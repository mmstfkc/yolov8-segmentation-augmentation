import argparse
from ColorBaseAugmentation import ColorBaseAugmentation


class Saturation(ColorBaseAugmentation):
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
        super().__init__(
            base_path,
            destination_path,
            saturation,
            min_saturation,
            max_saturation,
            count,
            min_saturation_count,
            max_saturation_count,
        )

        self.methodName = 'Saturation'


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
