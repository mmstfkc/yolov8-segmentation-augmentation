from BaseAugmentation import BaseAugmentation
import random
import numpy as np
import cv2
from BlurryAndLightCheck import BlurryAdnLightCheck


class ColorBaseAugmentation(BaseAugmentation):
    def __init__(
            self,
            base_path,
            destination_path,
            simple_range=None,
            min_range=None,
            max_range=None,
            simple_count=None,
            min_count=None,
            max_count=None,
    ):
        super().__init__(base_path, destination_path)

        self.blur_light = BlurryAdnLightCheck()
        self.image_light = None

        if simple_count:
            self.count1 = simple_count // 2
            self.count2 = simple_count // 2

            if simple_count % 2 == 1:
                self.count1 += 1
        else:
            self.count1 = min_count
            self.count2 = max_count

        self.total_count = self.count1 + self.count2

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

    def normalize_min_max_range(self, file_name):
        if self.image_light is None:
            self.image_light, _ = self.blur_light.image_preprocessing(file_name, self.base_image_path, self.methodName)

        min1, max2 = self.min_range1, self.max_range2

        if self.image_light == 0:  # Darkness
            if self.methodName in ['Hue', 'Exposure']:
                min1 = max(min1, 0.9)
            elif self.methodName in ['Saturation', 'Brightness']:
                min1 = max(min1, 0.5)

        return min1, (min1 + max2) / 2, (min1 + max2) / 2, max2

    def get_range_rate(self, file_name, part=None):
        normalize_min1, normalize_max1, normalize_min2, normalize_max2 = self.normalize_min_max_range(file_name)
        after_dot = 4

        if part == 1:
            return round(random.uniform(normalize_min1, normalize_max1), after_dot)
        elif part == 2:
            return round(random.uniform(normalize_min2, normalize_max2), after_dot)
        else:
            return round(random.uniform(normalize_min1, normalize_max2), after_dot)

    def process(self):
        # self.info()
        image_paths = self.get_images_from_file()

        for image_path in image_paths:
            image, file_name, file_extension = self.get_image_and_info(image_path)

            if self.total_count == 1:
                self.main_process(image, file_name, file_extension, 1)
            else:
                self.main_process(image, file_name, file_extension, self.count1, 1)

                self.main_process(image, file_name, file_extension, self.count2, 2)
            self.image_light = None

        print(f"{self.methodName} process is completed.")
        print('*' * 100)

    def main_process(self, image, file_name, file_extension, count, part=None):
        for _ in range(count):
            factor_rate = self.get_range_rate(f'{file_name}.{file_extension}', part)
            new_file_name = self.image_process(image, file_name, file_extension, factor_rate)
            self.copy_txt(file_name, new_file_name)

    def image_process(self, image, file_name, file_extension, factor_rate):
        # Convert image from BGR to HSL color space
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        return self.image_create_and_save(converted_image, file_name, file_extension, factor_rate)

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

    def create_multiple_image(self):
        image_paths = self.get_images_from_file()

        for image_path in image_paths:
            for i in range(500):
                image, file_name, file_extension = self.get_image_and_info(image_path)

                converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                self.image_create_and_save(converted_image, file_name, file_extension, i / 100)

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
