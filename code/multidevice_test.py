import datetime
from PIL import Image, ImageFont, ImageSequence
import time
import sys

from luma.core import virtual
from luma.core.sprite_system import framerate_regulator

from utils import devices


def now() -> str:
    return datetime.datetime.now().strftime('%H:%M')


def show_instructions(term) -> None:
    term.clear()

    term.println('READY!')
    term.println('------')

    term.println('Motion -> Spin Spin')
    term.println('Key1 -> Ring Ring')
    term.println('Key2 -> Meow Meow')
    term.println('Key3 -> Quit')

    term.println()


def spin(servo, num: int) -> None:
    """Spin a servo `num` times"""
    for _ in range(num):
        servo.max()
        time.sleep(.5)
        servo.min()
        time.sleep(.5)


def get_pressed(buttons) -> int:
    """Return index of pressed button or -1 if none are pressed
    """
    for i, button in enumerate(buttons):
        if button.is_pressed:
            return i

    return -1


def cat_jam(display, seconds: float):
    regulator = framerate_regulator(10)
    gif = Image.open('images/nyan-cat-rainbow.gif')
    size = [min(*display.size)] * 2
    posn = ((display.width - size[0]) // 2, display.height - size[1])

    start = time.time()

    while True:
        for frame in ImageSequence.Iterator(gif):
            with regulator:
                background = Image.new('RGB', display.size, 'black')
                background.paste(frame.resize(size, resample=Image.LANCZOS),
                                 posn)
                display.display(background.convert(display.mode))

            # print(f'{regulator.effective_FPS():.3f}')
            if time.time() - start >= seconds:
                return


def main():
    # setup
    display = devices.Display()

    pir = devices.MotionSensor()
    buttons = [devices.Button(num) for num in [0, 1, 2]]

    motor = devices.Motor()
    servo = devices.Servo(0)
    servo.min()

    font = ImageFont.truetype('fonts/ProggyTiny.ttf', 16)
    term = virtual.terminal(display, font)

    show_instructions(term)
    start = time.time()

    while True:

        if pir.motion_detected:
            spin(servo, 3)
            term.puts(f'\rHehe... nice'.ljust(term.width))

        selection = get_pressed(buttons)

        if selection > -1:
            if selection == 0:
                start = time.time()
                motor.on()

                buttons[0].wait_for_release()
                end = time.time()
                motor.off()

                term.puts(f'\rYou peed for {end-start:.2f}s'.ljust(term.width))

            if selection == 1:
                cat_jam(display, 4)
                term.puts('\rDid you just poop?'.ljust(term.width))

            if selection == 2:
                term.puts('\rBye bye!'.ljust(term.width))
                time.sleep(1)
                sys.exit()

        # impose max. frame rate
        time.sleep(1 / 30)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ...