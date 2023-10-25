import argparse
from ColorBaseAugmentation import ColorBaseAugmentation


class Exposure(ColorBaseAugmentation):
    def __init__(self,
                 base_path,
                 destination_path,
                 exposure=1,
                 min_exposure=None,
                 max_exposure=None,
                 count=1,
                 min_exposure_count=None,
                 max_exposure_count=None,
                 ):
        super().__init__(
            base_path,
            destination_path,
            exposure,
            min_exposure,
            max_exposure,
            count,
            min_exposure_count,
            max_exposure_count,
        )

        self.methodName = 'Exposure'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Specify source and destination paths when running your code.")

    parser.add_argument("--base_path", required=True)
    parser.add_argument("--destination_path", required=True)
    parser.add_argument("--exposure", required=False, default=1)
    parser.add_argument("--min_exposure", required=False, default=None)
    parser.add_argument("--max_exposure", required=False, default=None)
    parser.add_argument("--count", required=False, default=1)
    parser.add_argument("--min_exposure_count", required=False, default=None)
    parser.add_argument("--max_exposure_count", required=False, default=None)

    args = parser.parse_args()
    s = Exposure(
        args.base_path,
        args.destination_path,
        args.exposure,
        args.min_exposure,
        args.max_exposure,
        args.count,
        args.min_exposure_count,
        args.max_exposure_count
    )
