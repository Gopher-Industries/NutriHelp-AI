from torch.utils.data import DataLoader
from torchvision import transforms
from dataset import VFNDataset

def get_vfn_dataloaders(data_dir="processed", batch_size=32, image_size=(224, 224)):
    train_transform = transforms.Compose([
        transforms.Resize(image_size),
        # transforms.RandomRotation(15),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    val_test_transform = transforms.Compose([
        transforms.Resize(image_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    train_dataset = VFNDataset(
        csv_file=f"{data_dir}/train.csv",
        classes_file=f"{data_dir}/classes.json",
        transform=train_transform
    )

    val_dataset = VFNDataset(
        csv_file=f"{data_dir}/val.csv",
        classes_file=f"{data_dir}/classes.json",
        transform=val_test_transform
    )

    test_dataset = VFNDataset(
        csv_file=f"{data_dir}/test.csv",
        classes_file=f"{data_dir}/classes.json",
        transform=val_test_transform
    )

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4, pin_memory=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=4, pin_memory=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=4, pin_memory=True)

    return train_loader, val_loader, test_loader
