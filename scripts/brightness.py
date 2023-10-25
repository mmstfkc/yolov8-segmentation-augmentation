import argparse
from ColorBaseAugmentation import ColorBaseAugmentation


class Brightness(ColorBaseAugmentation):
    def __init__(self,
                 base_path,
                 destination_path,
                 brightness=1,
                 min_brightness=None,
                 max_brightness=None,
                 count=1,
                 min_brightness_count=None,
                 max_brightness_count=None,
                 ):
        super().__init__(
            base_path,
            destination_path,
            brightness,
            min_brightness,
            max_brightness,
            count,
            min_brightness_count,
            max_brightness_count,
        )

        self.methodName = 'Brightness'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Specify source and destination paths when running your code.")

    parser.add_argument("--base_path", required=True)
    parser.add_argument("--destination_path", required=True)
    parser.add_argument("--brightness", required=False, default=1)
    parser.add_argument("--min_brightness", required=False, default=None)
    parser.add_argument("--max_brightness", required=False, default=None)
    parser.add_argument("--count", required=False, default=1)
    parser.add_argument("--min_brightness_count", required=False, default=None)
    parser.add_argument("--max_brightness_count", required=False, default=None)

    args = parser.parse_args()
    s = Brightness(
        args.base_path,
        args.destination_path,
        args.brightness,
        args.min_brightness,
        args.max_brightness,
        args.count,
        args.min_brightness_count,
        args.max_brightness_count
    )
