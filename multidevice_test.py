import datetime
import PIL
import time

from luma.core import virtual

from utils import devices


def now() -> str:
    return datetime.datetime.now().strftime('%H:%M')


def main():
    button = devices.Button(0)
    motor = devices.Motor()
    display = devices.Display()

    font = PIL.ImageFont.truetype('fonts/ProggyTiny.ttf', 16)
    term = virtual.terminal(display, font)

    term.println('READY!')
    term.println('------')

    term.println('Try pressing Key1 :)')

    while True:
        term.println()

        button.wait_for_press()
        start = time.time()
        term.println(now() + ' Ring bell')
        motor.on()

        button.wait_for_release()
        end = time.time()
        term.println(now() + f' Stop ({end-start:.2f}s)')
        motor.off()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ...