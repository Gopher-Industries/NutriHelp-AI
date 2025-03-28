from torchutils import *
from torchvision import datasets, models, transforms
import os.path as osp
import os
if torch.cuda.is_available():
    device = torch.device('cuda:0')
else:
    device = torch.device('cpu')
print(f'Using device: {device}')
seed = 42
os.environ['PYTHONHASHSEED'] = str(seed)
np.random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = True
data_path = "F:\多媒体大作业\Food model\Crawler_split" #data set


params = {
    'model': 'resnet50d',  # Select the pre-trained model
    "img_size": 224,  # Picture input size
    "train_dir": osp.join(data_path, "train"),  #Training set path
    "val_dir": osp.join(data_path, "val"),  #val set path
    'device': device,  # device
    'lr': 1e-3,  # Learning rate
    'batch_size': 4,  # Batch size
    'num_workers': 0,
    'epochs': 15,  # epochs
    "save_dir": "../checkpoints/",  # Save path
    "pretrained": True,
     "num_classes": len(os.listdir(osp.join(data_path, "train"))),  # Number of food
    'weight_decay': 1e-5  # Learning rate attenuation
}


class SELFMODEL(nn.Module):
    def __init__(self, model_name=params['model'], out_features=params['num_classes'],
                 pretrained=True):
        super().__init__()
        pretrained_cfg=timm.models.create_model("resnet50d").default_cfg
        pretrained_cfg[
           'file']="F:\多媒体大作业\Food model\checkpoints/resnet50d_pretrained_224/resnet50d_14epochs_accuracy0.99144_weights.pth"
        self.model=timm.create_model(model_name,pretrained=pretrained,
                                     pretrained_cfg=pretrained_cfg)
        # classifier
        if model_name[:3] == "res":
            n_features = self.model.fc.in_features  # Example Change the number of fully connected layers
            self.model.fc = nn.Linear(n_features, out_features)  #Change the value to the number of categories corresponding to the task
        elif model_name[:3] == "vit":
            n_features = self.model.head.in_features
            self.model.head = nn.Linear(n_features, out_features)
        else:
            n_features = self.model.classifier.in_features
            self.model.classifier = nn.Linear(n_features, out_features)

        print(self.model)  # return model

    def forward(self, x):
        x = self.model(x)
        return x


# Define the training process
def train(train_loader, model, criterion, optimizer, epoch, params):
    metric_monitor = MetricMonitor()
    model.train()
    nBatch = len(train_loader)
    stream = tqdm(train_loader)
    for i, (images, target) in enumerate(stream, start=1):  # start
        images = images.to(params['device'], non_blocking=True)  # load data
        target = target.to(params['device'], non_blocking=True)  # load model
        output = model(images)
        loss = criterion(output, target.long())
        f1_macro = calculate_f1_macro(output, target)
        recall_macro = calculate_recall_macro(output, target)  # recall
        acc = accuracy(output, target)  # Accuracy score
        metric_monitor.update('Loss', loss.item())  # Replacement loss
        metric_monitor.update('F1', f1_macro)  # f1
        metric_monitor.update('Recall', recall_macro)  # update recall
        metric_monitor.update('Accuracy', acc)  # update acc
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()  #
        lr = adjust_learning_rate(optimizer, epoch, params, i, nBatch)  # Adjusted learning rate
        stream.set_description(
            "Epoch: {epoch}. Train.      {metric_monitor}".format(
                epoch=epoch,
                metric_monitor=metric_monitor)
        )
    return metric_monitor.metrics['Accuracy']["avg"], metric_monitor.metrics['Loss']["avg"]  # return result



def validate(val_loader, model, criterion, epoch, params):
    metric_monitor = MetricMonitor()
    model.eval()
    stream = tqdm(val_loader)
    with torch.no_grad():
        for i, (images, target) in enumerate(stream, start=1):
            images = images.to(params['device'], non_blocking=True)
            target = target.to(params['device'], non_blocking=True)
            output = model(images)
            loss = criterion(output, target.long())  # loss
            f1_macro = calculate_f1_macro(output, target)  # f1
            recall_macro = calculate_recall_macro(output, target)  # recall
            acc = accuracy(output, target)  # acc
            metric_monitor.update('Loss', loss.item())
            metric_monitor.update('F1', f1_macro)
            metric_monitor.update("Recall", recall_macro)
            metric_monitor.update('Accuracy', acc)
            stream.set_description(
                "Epoch: {epoch}. Validation. {metric_monitor}".format(
                    epoch=epoch,
                    metric_monitor=metric_monitor)
            )
    return metric_monitor.metrics['Accuracy']["avg"], metric_monitor.metrics['Loss']["avg"]



def show_loss_acc(acc, loss, val_acc, val_loss, sava_dir):
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.ylabel('Accuracy')
    plt.ylim([min(plt.ylim()), 1])
    plt.title('Training and Validation Accuracy')

    plt.subplot(2, 1, 2)
    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.ylabel('Cross Entropy')
    plt.title('Training and Validation Loss')
    plt.xlabel('epoch')

    save_path = osp.join(save_dir, "results.png")
    plt.savefig(save_path, dpi=100)


if __name__ == '__main__':
    accs = []
    losss = []
    val_accs = []
    val_losss = []
    data_transforms = get_torch_transforms(img_size=params["img_size"])
    train_transforms = data_transforms['train']
    valid_transforms = data_transforms['val']
    train_dataset = datasets.ImageFolder(params["train_dir"], train_transforms)  # 加载训练集
    valid_dataset = datasets.ImageFolder(params["val_dir"], valid_transforms)  # 加载验证集
    if params['pretrained'] == True:
        save_dir = osp.join(params['save_dir'], params['model']+"_pretrained_" + str(params["img_size"]))  # Set the model save path
    else:
        save_dir = osp.join(params['save_dir'], params['model'] + "_nopretrained_" + str(params["img_size"]))  # Set the model save path
    if not osp.isdir(save_dir):
        os.makedirs(save_dir)
        print("save dir {} created".format(save_dir))
    train_loader = DataLoader(  # Load the training set by batch
        train_dataset, batch_size=params['batch_size'], shuffle=True,
        num_workers=params['num_workers'], pin_memory=True,
    )
    val_loader = DataLoader(  # Load the validation set by batch
        valid_dataset, batch_size=params['batch_size'], shuffle=False,
        num_workers=params['num_workers'], pin_memory=True,
    )
    print(train_dataset.classes)
    model = SELFMODEL(model_name=params['model'], out_features=params['num_classes'],
                 pretrained=params['pretrained']) # Loading model
    # model = nn.DataParallel(model)  # Model parallelization to improve model speed
    # resnet50d_1epochs_accuracy0.50424_weights.pth
    model = model.to(params['device'])
    criterion = nn.CrossEntropyLoss().to(params['device'])  #
    optimizer = torch.optim.AdamW(model.parameters(), lr=params['lr'], weight_decay=params['weight_decay'])

    # criterion = nn.CrossEntropyLoss().to(params['device'])  # Set loss function
    # optimizer = torch.optim.AdamW(model.parameters(), lr=params['lr'], weight_decay=params['weight_decay'])
    best_acc = 0.0  # Record the best accuracy
    # The one with the best preservation.。
    for epoch in range(1, params['epochs'] + 1):  # start
        acc, loss = train(train_loader, model, criterion, optimizer, epoch, params)
        val_acc, val_loss = validate(val_loader, model, criterion, epoch, params)
        accs.append(acc)
        losss.append(loss)
        val_accs.append(val_acc)
        val_losss.append(val_loss)
        if val_acc >= best_acc:

            save_path = osp.join(save_dir, f"{params['model']}_{epoch}epochs_accuracy{acc:.5f}_weights.pth")
            torch.save(model.state_dict(), save_path)
            best_acc = val_acc
    show_loss_acc(accs, losss, val_accs, val_losss, save_dir)
    print("The training has been completed, and the model and training logs are saved in: {}".format(save_dir))
