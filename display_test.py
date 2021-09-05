from luma.core.render import canvas

import time

from utils import devices

if __name__ == '__main__':
    display = devices.Display()
    
    with canvas(display) as draw:
        draw.rectangle(display.bounding_box, outline='white', fill='blue')
        draw.text((30, 40), 'Hello World', fill='white')

    time.sleep(5)
    display.backlight(False)
    time.sleep(2)
