import os

from saturation import Saturation
from flip import Flip
from brightness import Brightness
from hue import Hue
from exposure import Exposure

if __name__ == "__main__":
    base_path = "base_path"
    destination_path = "destination_path"

    count = 10

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

    brightness.process()
    saturation.process()
    hue.process()
    exposure.process()

    for i in range(3):
        flip = Flip(base_path, destination_path, i)
        flip.process()

    base_file_count = len([i for i in os.listdir(f'{base_path}images') if i.endswith('jpg') or i.endswith('jpeg')])
    destination_file_count = len(
        [i for i in os.listdir(f'{destination_path}images') if i.endswith('jpg') or i.endswith('jpeg')])

    file_count = (base_file_count * ((4 * count) + 1)) + (base_file_count * 3)

    print()
    print(f'Base file count:{base_file_count}.')
    print(f'Destination file count:{destination_file_count}.')
    print(f'Olması gereken sayı:{file_count}')
