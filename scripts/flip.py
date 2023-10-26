import cv2
import argparse
from BaseAugmentation import BaseAugmentation


class Flip(BaseAugmentation):
    def __init__(self, base_path, destination_path, flip_type=1):
        super().__init__(base_path, destination_path)

        self.flip_names = ['Vertical', 'Horizontal', 'Vertical And Horizontal']
        self.flip_type = flip_type
        self.methodName = 'Flip'

    # The location where we wrote the flipped data to a new text file.
    def save_new_txt(self, new_file_name, flipped_segmentation_data):
        with open(f'{self.destination_label_path + new_file_name}.txt', "w") as output_file:
            for class_id, coords in flipped_segmentation_data:
                coords_str = ' '.join(map(str, [class_id] + coords))
                output_file.write(f"{coords_str}\n")

    @staticmethod
    def horizontal_flip(coords):
        # Vertical flip operation (keep x coordinates the same, reverse y coordinates)
        return [1 - coords[i] if i % 2 == 0 else coords[i] for i in range(len(coords))]

    @staticmethod
    def vertical_flip(coords):
        # Vertical flip operation (reverse x coordinates, keep y coordinates the same)
        return [1.0 - coord if i % 2 == 1 else coord for i, coord in enumerate(coords)]

    @staticmethod
    def horizontal_and_vertical_flip(coords):
        # Horizontal and Vertical flip operation
        return [1.0 - coord for coord in coords]

    # The place where we filled the content of a new text file with the flipped data.
    def create_new_txt(self, file_name, new_file_name):
        with open(f'{self.base_label_path + file_name}.txt', "r") as file:
            lines = file.readlines()
            flipped_segmentation_data = []
            for line in lines:
                parts = line.split()
                class_id = int(parts[0])
                coords = [float(coord) for coord in parts[1:]]

                if self.flip_type == 1:
                    flipped_coords = self.horizontal_flip(coords)
                elif self.flip_type == 0:
                    flipped_coords = self.vertical_flip(coords)
                else:
                    flipped_coords = self.horizontal_and_vertical_flip(coords)

                flipped_segmentation_data.append((class_id, flipped_coords))

        self.save_new_txt(new_file_name, flipped_segmentation_data)

    # Return flipped image
    def create_flipped_image(self, image):
        if self.flip_type in [1, 0]:
            flipped_image = cv2.flip(image, self.flip_type)
        else:
            flipped_image = cv2.flip(image, 1)
            flipped_image = cv2.flip(flipped_image, 0)

        return flipped_image

    def process(self):
        print(f'{self.methodName} by {self.flip_names[self.flip_type]} process started...')

        image_paths = self.get_images_from_file()

        for image_path in image_paths:
            image, file_name, file_extension = self.get_image_and_info(image_path)
            new_file_name = self.get_new_name_format(
                file_name,
                str(self.flip_names[self.flip_type]).lower().replace(' ', '-')
            )

            self.create_new_txt(file_name, new_file_name)

            flipped_image = self.create_flipped_image(image)
            self.save_image(new_file_name, file_extension, flipped_image)

            self.save_image(file_name, file_extension, image)
            self.copy_txt(file_name, file_name)

        print(f'{self.methodName} by {self.flip_names[self.flip_type]} process competed.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Specify source and destination paths when running your code.")

    parser.add_argument("--base_path", required=True)
    parser.add_argument("--destination_path", required=True)
    parser.add_argument("--flip_type", required=False, default=1)
    # (1 Horizontal) (0 Vertical) (2 Vertical And Horizontal)

    args = parser.parse_args()
    f = Flip(args.base_path, args.destination_path, args.flip_type)
