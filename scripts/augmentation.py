import os
from saturation import Saturation
from flip import Flip
from brightness import Brightness
from hue import Hue
from exposure import Exposure

if __name__ == "__main__":
    base_path = "/Users/mustafakoc/Desktop/yolov8-segmentation-augmentation/images"
    destination_path = "/Users/mustafakoc/Desktop/yolov8-segmentation-augmentation/images2"
    count = 2

    saturation = Saturation(
        base_path,
        destination_path,
        min_saturation=0.6,
        max_saturation=1.6,
        count=count
    )

    brightness = Brightness(
        base_path,
        destination_path,
        min_brightness=0.75,
        max_brightness=1.2,
        count=count
    )

    hue = Hue(
        base_path,
        destination_path,
        min_hue=0.9,
        max_hue=1.1,
        count=count
    )

    exposure = Exposure(
        base_path,
        destination_path,
        min_exposure=0.9,
        max_exposure=1.0,
        count=count
    )

    brightness.mix(saturation.mix(hue.mix(exposure.mix(count=1), count=1), count=1), True)
    flip = Flip(base_path, destination_path, 1)
    brightness.mix(flip.mix(), True)

    # brightness.process()
    # saturation.process()
    # hue.process()
    # exposure.process()

    # for i in range(3):
    #    flip = Flip(base_path, destination_path, i)
    #    flip.process()
