from ultralytics import YOLO

model = YOLO(r"Food-Detection\dataset\runs\detect\train2\weights\best.pt")
image_path = r"Food-Detection\dataset\images\test\3_jpg.rf.f2a1a102a11832ae1d2d6edf055f020d.jpg"
result = model(
    image_path, save=True,  iou=0.5)

