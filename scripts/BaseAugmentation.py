import cv2
import os
import shutil


class BaseAugmentation:
    def __init__(self, base_path, destination_path):
        self.base_path = base_path
        self.destination_path = destination_path

        self.non_mixed_base_path = base_path
        self.non_mixed_destination_path = destination_path
        self.mix_deep_rate = 0

        self.base_image_path = os.path.join(base_path, 'images/')
        self.base_label_path = os.path.join(base_path, 'labels/')

        self.destination_image_path = os.path.join(destination_path, 'images/')
        self.destination_label_path = os.path.join(destination_path, 'labels/')

        self.methodName = None

        os.makedirs(self.destination_image_path, exist_ok=True)
        os.makedirs(self.destination_label_path, exist_ok=True)

    def update_base_destination_path(self):
        self.base_image_path = os.path.join(self.base_path, 'images/')
        self.base_label_path = os.path.join(self.base_path, 'labels/')

        self.destination_image_path = os.path.join(self.destination_path, 'images/')
        self.destination_label_path = os.path.join(self.destination_path, 'labels/')

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

    def process(self):
        pass

    def mixin(self, classes=None, is_last=False):
        if classes:
            if isinstance(classes, BaseAugmentation):
                self.mix_deep_rate += classes.mix_deep_rate + 1
                self.base_path = classes.destination_path[:-1] + str(self.mix_deep_rate - 1)
                self.destination_path = classes.destination_path[:-1] + str(self.mix_deep_rate)
                self.update_base_destination_path()
                self.process()

                if is_last:
                    self.copy_folder(self.destination_path)
                    shutil.rmtree(self.destination_path)
                    self.copy_folder(self.non_mixed_base_path)
                return self
            else:
                return None
        else:
            self.destination_path = os.path.join(self.destination_path, f'm/{str(self.mix_deep_rate)}')
            self.update_base_destination_path()
            self.process()
            return self

    def copy_folder(self, source):
        for folder, sub_folder, files in os.walk(source):
            for file in files:
                file_path = os.path.join(folder, file)

                destination_file_path = os.path.join(self.non_mixed_destination_path,
                                                     os.path.relpath(file_path, source))
                os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)

                shutil.copy2(file_path, destination_file_path)
