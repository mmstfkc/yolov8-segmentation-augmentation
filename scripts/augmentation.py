from saturation import Saturation
from flip import Flip
from brightness import Brightness
from hue import Hue
from exposure import Exposure

if __name__ == "__main__":
    base_path = "base_path"
    destination_path = "destination_path"
    count = 2

    saturation = Saturation(
        base_path,
        destination_path,
        min_saturation=0.4,
        max_saturation=2.4,
        count=count
    )

    brightness = Brightness(
        base_path,
        destination_path,
        min_brightness=0.2,
        max_brightness=1.3,
        count=count
    )

    hue = Hue(
        base_path,
        destination_path,
        min_hue=0.8,
        max_hue=1.4,
        count=count
    )

    exposure = Exposure(
        base_path,
        destination_path,
        min_exposure=0.4,
        max_exposure=1.1,
        count=count
    )

    # Mixing using example1
    # brightness.mix(saturation.mix(hue.mix(exposure.mix(count=1), count=1), count=1), True)

    # Mixing using example2
    flip = Flip(base_path, destination_path, 1)
    # brightness.mix(flip.mix(), True)

    # One Method using example1
    brightness.process()
    saturation.process()
    hue.process()
    exposure.process()

    # One Method using example2
    # 0 => Vertical
    # 1 => Horizontal
    # 2 => Vertical And Horizontal
    # for i in range(3):
    #    flip = Flip(base_path, destination_path, i)
    #    flip.process()
