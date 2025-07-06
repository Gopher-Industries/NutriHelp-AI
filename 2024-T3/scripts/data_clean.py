import shutil
import cv2
import os
import os.path as osp
import numpy as np
from tqdm import tqdm


def cv_imread(file_path, type=-1):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    if type == 0:
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    return cv_img

def cv_imwrite(file_path, cv_img, is_gray=True):
    if len(cv_img.shape) == 3 and is_gray:
        cv_img = cv_img[:, :, 0]
    cv2.imencode(file_path[-4:], cv_img)[1].tofile(file_path)

# The data cleaning function handles all subfolders under the main folder
def data_clean(src_folder):
    # Create a home folder to save the cleaned images
    clean_folder = src_folder + "_cleaned"
    if os.path.isdir(clean_folder):
        print("The cleared save directory already exists")
        shutil.rmtree(clean_folder)
    os.mkdir(clean_folder)

    # Iterate through all the subfolders in the main folder
    for sub_folder in os.listdir(src_folder):
        sub_folder_path = osp.join(src_folder, sub_folder)
        if not os.path.isdir(sub_folder_path):
            continue  # Skip non-folder items

        # Use the original English name as the cleaning path for the subfolder
        sub_clean_folder = osp.join(clean_folder, sub_folder)
        os.mkdir(sub_clean_folder)

        image_names = os.listdir(sub_folder_path)
        with tqdm(total=len(image_names), desc=f"Processing {sub_folder}") as pabr:
            for i, image_name in enumerate(image_names):
                image_path = osp.join(sub_folder_path, image_name)
                try:
                    img = cv_imread(image_path)
                    img_channel = img.shape[-1]
                    if img_channel == 3:
                        save_image_name = sub_folder + "_" + str(i) + ".jpg"
                        save_path = osp.join(sub_clean_folder, save_image_name)
                        cv_imwrite(file_path=save_path, cv_img=img, is_gray=False)
                except Exception as e:
                    print(f"{image_name} is bad: {e}")
                pabr.update(1)

if __name__ == '__main__':
    # Pass in the main folder path and process all subfolders
    data_clean(src_folder="F://work//identification//Crawler")#data path
