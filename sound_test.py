from typing import Tuple

import argparse
import logging
import numpy as np
import sounddevice as sd
import soundfile as sf

logging.basicConfig(level=logging.INFO)

logging.info(sd.query_devices())


def _make_sine(duration: float,
               amplitude: float,
               frequency: int,
               sampling_freq: float,
               save_plot: bool = False) -> Tuple[np.ndarray, float]:
    """Make sine wave

    Args:
        duration (float): duration in seconds
        amplitude (float): amplitude (ranges from -1 to 1)
        frequency (int): frequency in Hertz
        sampling_freq (float): sampling frequency in Hertz
        save_plot (bool, optional): whether to save a plot of the first 200 samples. Defaults to False.

    Returns:
        Tuple[np.ndarray, float]: numpy array & sampling frequency
    """
    # https://nbviewer.jupyter.org/github/mgeier/python-audio/blob/master/simple-signals.ipynb
    # x = time points, f(x) = sine
    t = np.arange(duration, step=1 / sampling_freq)
    sine = amplitude * np.sin(2 * np.pi * frequency * t)

    # plot
    if save_plot:
        import matplotlib.pyplot as plt

        plt.plot(t[:200] * 1000, sine[:200])
        plt.xlabel('time / milliseconds')
        plt.ylim(-1.1, 1.1)
        # plt.show()
        plt.savefig(f'sine_{frequency}hz.png')

    return sine, sampling_freq


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    # if input file is provided, play it; else play sine tone
    parser.add_argument('-i', '--input-file')
    
    # if output file is provided, record for specified duration
    parser.add_argument('-o', '--output-file')
    parser.add_argument('-d', '--output-duration', type=int, default=3)

    args, _ = parser.parse_known_args()

    return args


if __name__ == '__main__':
    # parse command line arguments
    args = _parse_args()
    logging.info(args)

    # get audio data
    if args.input_file is None:
        # make it
        data, fs = _make_sine(duration=1,
                              amplitude=.1,
                              frequency=440,
                              sampling_freq=44100)
    else:
        # from file
        data, fs = sf.read(args.input_file, always_2d=True)

    # play it
    logging.info('playing')
    sd.play(data, fs)
    sd.wait()

    # record
    if args.output_file is not None:
        logging.info('recording')

        fs = 44100
        data_out = sd.rec(int(args.output_duration * fs),
                          samplerate=fs,
                          channels=2)
        sd.wait()

        # write to file
        sf.write(args.output_file, data_out, fs)
