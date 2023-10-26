import cv2
import os
import shutil


class BaseAugmentation:
    def __init__(self, base_path, destination_path):
        self.base_image_path = os.path.join(base_path, 'images/')
        self.base_label_path = os.path.join(base_path, 'labels/')

        self.destination_image_path = os.path.join(destination_path, 'images/')
        self.destination_label_path = os.path.join(destination_path, 'labels/')

        self.methodName = None

        os.makedirs(self.destination_image_path, exist_ok=True)
        os.makedirs(self.destination_label_path, exist_ok=True)

    @staticmethod
    def check_min_max_value(value1, value2):
        return (value2, value1) if value1 > value2 else (value1, value2)

    def get_new_name_format(self, file_name, rate):
        return f'{file_name}-{str(self.methodName).lower()}-{rate}'

    def get_image_and_info(self, image_path):
        image = cv2.imread(self.base_image_path + image_path)
        file_name, image_extension = os.path.splitext(os.path.basename(image_path))

        return image, file_name, image_extension[1:]

    def get_images_from_file(self):
        return [f for f in os.listdir(self.base_image_path) if f.endswith((".jpg", ".jpeg"))]

    def save_image(self, new_file_name, file_extension, new_image):
        cv2.imwrite(os.path.join(self.destination_image_path, f"{new_file_name}.{file_extension}"), new_image)

    def copy_txt(self, file_name, new_file_name):
        shutil.copy(f'{self.base_label_path + file_name}.txt', f'{self.destination_label_path + new_file_name}.txt')
