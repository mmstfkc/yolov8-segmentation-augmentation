from BaseAugmentation import BaseAugmentation
import random
import shutil
import numpy as np
import cv2


class ColorBaseAugmentation(BaseAugmentation):
    def __init__(
            self,
            base_path,
            destination_path,
            simple_range=50,
            min_range=None,
            max_range=None,
            simple_count=1,
            min_count=None,
            max_count=None,
    ):
        super().__init__(base_path, destination_path)

        if simple_count:
            self.count1 = simple_count // 2
            self.count2 = simple_count // 2

            if simple_count % 2 == 1:
                self.count1 += 1
        else:
            self.count1 = min_count
            self.count2 = max_count

        if simple_range:
            self.min_range1 = 0
            self.max_range1 = simple_range / 2

            self.min_range2 = simple_range / 2
            self.max_range2 = simple_range
        else:
            min_range, max_range = self.check_min_max_value(max_range, min_range)

            self.min_range1 = min_range
            self.max_range1 = (min_range + max_range) / 2

            self.min_range2 = (min_range + max_range) / 2
            self.max_range2 = max_range

        self.normalize_min_max_range()

    def normalize_min_max_range(self):
        if self.methodName == 'Saturation':
            pass
        elif self.methodName == 'Hue':
            pass
        elif self.methodName == 'Exposure':
            pass
        elif self.methodName == 'Brightness':
            pass
        else:
            pass

    def get_range_rate(self, part=None):
        if part == 1:
            return round(random.uniform(self.min_range1, self.max_range1), 2)
        else:
            return round(random.uniform(self.min_range2, self.max_range2), 2)

    def process(self):
        self.info()
        image_paths = self.get_images_from_file()

        for image_path in image_paths:

            for _ in range(self.count1):
                file_name, new_file_name = self.image_process(image_path, 1)
                self.copy_txt(file_name, new_file_name)

            for _ in range(self.count2):
                file_name, new_file_name = self.image_process(image_path, 2)
                self.copy_txt(file_name, new_file_name)

        print(f"{self.methodName} process is completed.")
        print('*' * 100)

    def image_process(self, image_path, part):
        image, file_name, file_extension = self.get_image_and_info(image_path)
        factor_rate = self.get_range_rate(part)

        # Convert image from BGR to HSL color space
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        new_file_name = self.image_create_and_save(converted_image, file_name, file_extension, factor_rate)

        return file_name, new_file_name

    def image_create_and_save(self, converted_image, file_name, file_extension, factor_rate):
        if self.methodName == 'Saturation':
            processes_image = self.image_clip_process(converted_image, 1, factor_rate, 0, 255)
        elif self.methodName == 'Hue':
            processes_image = self.image_clip_process(converted_image, 0, factor_rate, 0, 179)
        elif self.methodName == 'Brightness':
            processes_image = self.image_clip_process(converted_image, 2, factor_rate, 0, 255)
        else:
            # Exposure
            processes_image = cv2.convertScaleAbs(converted_image, alpha=factor_rate, beta=0)

        # Convert HSL image back to BGR
        new_image = cv2.cvtColor(processes_image, cv2.COLOR_HSV2BGR)

        new_file_name = self.get_new_name_format(file_name, factor_rate)
        new_image_path = f'{self.destination_image_path}{new_file_name}.{file_extension}'

        cv2.imwrite(new_image_path, new_image)
        return new_file_name

    # cpt => color pixel point
    # 0 => Red
    # 1 => Green
    # 2 => Blue
    @staticmethod
    def image_clip_process(image, cpt, rate, a_min, a_max):
        image[:, :, cpt] = (np.clip(image[:, :, cpt] * rate, a_min, a_max))

        return image

    def copy_txt(self, file_name, new_file_name):
        shutil.copy(f'{self.base_label_path + file_name}.txt', f'{self.destination_label_path + new_file_name}.txt')

    def create_multiple_image(self):
        image_paths = self.get_images_from_file()
        image_path = image_paths[0]

        image, file_name, file_extension = self.get_image_and_info(image_path)
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        for i in range(100):
            counter = (i + 1) * 0.1  # 1.0 artırarak farklı değerler elde edin
            self.image_create_and_save(converted_image, file_name, file_extension, counter)

    def info(self):
        print(f'{self.methodName} process starting...')
        print('Part 1')
        print(f'\tCount:{self.count1}')
        print(f'\tMin {self.methodName} rate:{self.min_range1}.')
        print(f'\tMax {self.methodName} rate:{self.max_range1}.')
        print('Part 2')
        print(f'\tCount:{self.count2}')
        print(f'\tMin {self.methodName} rate:{self.min_range2}.')
        print(f'\tMax {self.methodName} rate:{self.max_range2}')
