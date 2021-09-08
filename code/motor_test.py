import argparse
import logging

from utils import devices

logging.basicConfig(level=logging.INFO)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument('--on', type=float, default=1)
    parser.add_argument('--off', type=float, default=1)
    parser.add_argument('--n', type=int, default=2)

    args, _ = parser.parse_known_args()

    return args


if __name__ == '__main__':
    # parse command line arguments
    args = _parse_args()
    logging.info(args)

    motor = devices.Motor()
    motor.blink(on_time=args.on, off_time=args.off, n=args.n, background=False)
