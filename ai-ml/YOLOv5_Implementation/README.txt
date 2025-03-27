yolov5 implementation by Ultralytics, Modified by Reeven Ajero for Gopher Nutrihelp: 
https://drive.google.com/drive/folders/1r68hArA2Q1kORNUN9ixwI3YhFcgydEpm?usp=sharing

Requires Pytorch and Python v3.11 or lower, do not Use 3.12 idk why, but it does not like it.
use CUDA 12.4
https://pytorch.org/get-started/locally/

Dataset:
-set up fruits 360 yaml in yolov5/data
-you can rename it
-place data set in /yolov5/data/datasets/
-modify 'path:' in yolov5/data/fruits360.yaml to match your dataset folder name
-set do not modify train/val/test it is better to change your folder structure to match it
-change names to fit your classes, order is important and must be the same order for your labels.

Training:
-there is a train.txt copy it and run the code in the command line in your environment where you installed the requirements.
-Modify --img for image size

Predict:
use detect.txt it is similar to training above. set the target img/video
