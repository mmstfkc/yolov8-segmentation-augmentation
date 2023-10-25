import argparse
from ColorBaseAugmentation import ColorBaseAugmentation


class Hue(ColorBaseAugmentation):
    def __init__(self,
                 base_path,
                 destination_path,
                 hue=1,
                 min_hue=None,
                 max_hue=None,
                 count=1,
                 min_hue_count=None,
                 max_hue_count=None,
                 ):
        super().__init__(
            base_path,
            destination_path,
            hue,
            min_hue,
            max_hue,
            count,
            min_hue_count,
            max_hue_count,
        )

        self.methodName = 'Hue'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Specify source and destination paths when running your code.")

    parser.add_argument("--base_path", required=True)
    parser.add_argument("--destination_path", required=True)
    parser.add_argument("--hue", required=False, default=1)
    parser.add_argument("--min_hue", required=False, default=None)
    parser.add_argument("--max_hue", required=False, default=None)
    parser.add_argument("--count", required=False, default=1)
    parser.add_argument("--min_hue_count", required=False, default=None)
    parser.add_argument("--max_hue_count", required=False, default=None)

    args = parser.parse_args()
    s = Hue(
        args.base_path,
        args.destination_path,
        args.hue,
        args.min_hue,
        args.max_hue,
        args.count,
        args.min_hue_count,
        args.max_hue_count
    )
