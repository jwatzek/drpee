import logging

from luma.core.render import canvas

from utils import devices

logging.basicConfig(level=logging.INFO)

button = devices.Button(0)
motor = devices.Motor()
display = devices.Display()

logging.info('Ready')


def main():
    while True:
        with canvas(display) as draw:
            draw.rectangle(display.bounding_box, outline='white', fill='blue')
            draw.text((30, 40),
                      'Ready! Key1',
                      fill='white')

        button.wait_for_press()
        logging.info('Ring bell')
        motor.on()

        with canvas(display) as draw:
            draw.rectangle(display.bounding_box, outline='white', fill='blue')
            draw.text((30, 80), 'Ringing!', fill='white')

        button.wait_for_release()
        logging.info('Stop')
        motor.off()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ...