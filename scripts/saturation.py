import random
import cv2
import numpy as np
import argparse
import shutil
from BaseAugmentation import BaseAugmentation


class Saturation(BaseAugmentation):
    def __init__(self,
                 base_path,
                 destination_path,
                 saturation=1,
                 min_saturation=None,
                 max_saturation=None,
                 count=1,
                 min_saturation_count=None,
                 max_saturation_count=None,
                 ):
        super().__init__(base_path, destination_path)

        self.methodName = 'Saturation'

        # Saturation Rate Process
        if saturation:
            self.min_saturation = abs(saturation) % 100
            self.max_saturation = abs(saturation) % 100
        else:
            self.min_saturation = abs(min_saturation) % 100
            self.max_saturation = abs(max_saturation) % 100

        self.check_min_max_saturation()
        self.min_saturation, self.max_saturation = self.check_min_max_value(self.max_saturation, self.min_saturation)

        # Saturation Count Parse Process
        if count:
            self.count1 = count
            self.count2 = count
        else:
            self.count1 = min_saturation_count
            self.count2 = max_saturation_count

        # Saturation Rate Parse Process
        if saturation == 1:
            self.min_saturation1 = 1
            self.max_saturation1 = 1

            self.min_saturation2 = 1
            self.max_saturation2 = 1
        else:
            self.min_saturation1 = self.min_saturation / 2
            self.max_saturation1 = self.max_saturation / 2

            self.min_saturation2 = self.max_saturation1
            self.max_saturation2 = self.max_saturation

        print('Saturation process starting...')
        print('Part 1')
        print(f'\tCount:{self.count1}')
        print(f'\tMin saturation rate:{self.min_saturation1}. Max saturation rate:{self.max_saturation1}')
        print('Part 2')
        print(f'\tCount:{self.count2}')
        print(f'\tMin saturation rate:{self.min_saturation2}. Max saturation rate:{self.max_saturation2}')
        self.main()
        print("Saturation process is completed.")

    def check_min_max_saturation(self):
        if self.min_saturation != 1.0 and self.max_saturation != 1.0:
            self.min_saturation = (100 - self.min_saturation) / 100
            self.max_saturation = self.max_saturation / 10

    def get_saturation_rate(self, part=None):
        if part == 1:
            return round(random.uniform(self.min_saturation1, self.max_saturation1), 2)
        else:
            return round(random.uniform(self.min_saturation2, self.max_saturation2), 2)

    @staticmethod
    def adjust_saturation(image, saturation_factor):
        # Convert image from BGR to HSL color space
        hsl_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

        # Change saturation
        hsl_image[:, :, 2] = np.clip(hsl_image[:, :, 2] * saturation_factor, 0, 255)

        # Convert HSL image back to BGR
        return cv2.cvtColor(hsl_image, cv2.COLOR_HLS2BGR)

    def saturation(self, image, image_name, image_extension, part=None):
        saturation_factor = self.get_saturation_rate(part)
        saturated_image = self.adjust_saturation(image, saturation_factor=saturation_factor)
        new_image_name = f"{image_name}-{self.methodName}-{str(saturation_factor).replace('.', ',')}"

        new_image_path = f'{self.destination_image_path}{new_image_name}.{image_extension}'
        cv2.imwrite(new_image_path, saturated_image)
        shutil.copy(f'{self.base_label_path + image_name}.txt', f'{self.destination_label_path + new_image_name}.txt')

    def main(self):
        image_paths = self.get_images_from_file()

        for image_path in image_paths:
            image, file_name, file_extension = self.get_image_and_info(image_path)

            for _ in range(self.count1):
                self.saturation(image, file_name, file_extension, 1)

            for _ in range(self.count2):
                self.saturation(image, file_name, file_extension, 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Specify source and destination paths when running your code.")

    parser.add_argument("--base_path", required=True)
    parser.add_argument("--destination_path", required=True)
    parser.add_argument("--saturation", required=False, default=1)
    parser.add_argument("--min_saturation", required=False, default=None)
    parser.add_argument("--max_saturation", required=False, default=None)
    parser.add_argument("--count", required=False, default=1)
    parser.add_argument("--min_saturation_count", required=False, default=None)
    parser.add_argument("--max_saturation_count", required=False, default=None)

    args = parser.parse_args()
    s = Saturation(
        args.base_path,
        args.destination_path,
        args.saturation,
        args.min_saturation,
        args.max_saturation,
        args.count,
        args.min_saturation_count,
        args.max_saturation_count
    )
