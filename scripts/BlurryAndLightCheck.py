from scipy.stats import entropy
import numpy as np
import cv2
import os
from ultralytics import YOLO
import matplotlib.pyplot as plt


class BlurryAdnLightCheck:
    # Image Blurry Checking #
    # Blur Detection with Image Entropy
    def calculate_image_entropy_img(self, image, min_entropy=3, max_entropy=10):
        entropy_value = entropy(image.ravel())

        return self.min_max_value(entropy_value, min_entropy, max_entropy)

    # Haze Detection with Variance Measurement
    def calculate_image_variance_img(self, image, min_variance=100, max_variance=5000):
        variance_value = cv2.Laplacian(image, cv2.CV_64F).var()

        return self.min_max_value(variance_value, min_variance, max_variance)

    # Turbidity Detection with Frequency Domain Analysis:
    def calculate_frequency_domain_analysis_img(self, image, min_frequency=3, max_frequency=10):
        f_transform = np.fft.fft2(image)
        f_transform_shifted = np.fft.fftshift(f_transform)

        magnitude_spectrum = np.log(np.abs(f_transform_shifted) + 1)

        return self.min_max_value(np.mean(magnitude_spectrum), min_frequency, max_frequency)

    def blur_info_img(self, image):
        pointer = 0
        pointer += self.calculate_image_entropy_img(image)
        pointer += self.calculate_image_variance_img(image)
        pointer += self.calculate_frequency_domain_analysis_img(image)

        return pointer

    @staticmethod
    def min_max_value(data, min_data, max_data):
        return 1 if max_data > data > min_data else 0

    @staticmethod
    # Image Light Checking
    def light_check(light_check_image):
        light_rate = light_check_image.mean()

        if light_rate < 40:
            return 0  # Darkness
        elif light_rate > 210:
            return 2  # Other
        else:
            return 1  # Normal

    @staticmethod
    def largest_vehicle_detection(image_path, method_name):
        #if method_name != 'Brightness':
        w, h, _ = cv2.imread(image_path).shape
        return 0, 0, w, h

        model = YOLO('yolov8x.pt')
        model_predict = model.predict(image_path)

        boxes_data = model_predict[0].boxes.cpu().numpy()
        class_ids = model_predict[0].boxes.cls.cpu().numpy()

        class_id = 0

        if class_id not in class_ids:
            w, h, _ = cv2.imread(image_path).shape
            return 0, 0, w, h

        selected_indices = [i for i, cls_id in enumerate(class_ids) if cls_id == class_id]

        selected_boxes = [boxes_data[i] for i in selected_indices]
        # Calculate the area of each box (e.g. width * height)
        areas = [
            ((box.data[0][2] - box.data[0][0]) ** 2)
            * ((box.data[0][3] - box.data[0][1]) ** 2) ** (1 / 2)
            for box in selected_boxes
        ]

        # Find the largest area
        max_area_index = areas.index(max(areas))

        # Select the box with the largest area
        selected_box = selected_boxes[max_area_index]

        return map(int, selected_box.data[0][:4])

    def image_preprocessing(self, filename, path, method_name):
        image_path = os.path.join(path, filename)

        x1, y1, x2, y2 = self.largest_vehicle_detection(image_path, method_name)

        gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Grayscale image
        p = self.blur_info_img(gray[y1:y2, x1:x2])

        light = self.light_check(gray[y1:y2, x1:x2])
        blur = self.min_max_range(p, 1, 4)

        return light, blur

    @staticmethod
    def min_max_range(data, min_range, max_range):
        return 1 if max_range > data > min_range else 0
