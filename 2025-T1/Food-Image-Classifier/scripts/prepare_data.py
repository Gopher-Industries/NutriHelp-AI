from torchvision.datasets import Food101
from torchvision import transforms
from torch.utils.data import DataLoader

def get_food101_dataloaders(data_dir='data', batch_size=32, image_size=(224, 224)):
    transform = transforms.Compose([
        transforms.Resize(image_size),
        transforms.RandomRotation(15),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5]*3, std=[0.5]*3)
    ])

    train_dataset = Food101(root=data_dir, split='train', download=True, transform=transform)
    test_dataset = Food101(root=data_dir, split='test', download=True, transform=transform)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    return train_loader, test_loader


get_food101_dataloaders()

