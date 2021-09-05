from typing import Tuple

import gpiozero
from luma.core.interface.serial import spi
from luma.lcd import device


class GPIO:
    MOTOR = 4

    KEY1 = 21
    KEY2 = 20
    KEY3 = 16

    JOY_UP = 6
    JOY_DOWN = 19
    JOY_LEFT = 5
    JOY_RIGHT = 26
    JOY_BUTTON = 13


class LCD:
    GPIO_SCLK = 11  # SPI clock
    GPIO_MOSI = 10  # SPI data
    GPIO_CE0 = 8  # SPI chip select
    GPIO_DATA_CMD = 25
    GPIO_RESET = 27
    GPIO_BACKLIGHT = 24

    WIDTH = 128
    HEIGHT = 128
    H_OFFSET = 1
    V_OFFSET = 2


class Display(device.st7735):
    """ST7735 display via SPI interface"""
    def __init__(self):
        interface = spi(port=0,
                        device=0,
                        gpio_DC=LCD.GPIO_DATA_CMD,
                        gpio_RST=LCD.GPIO_RESET)

        params = {
            'width': LCD.WIDTH,
            'height': LCD.HEIGHT,
            'h_offset': LCD.H_OFFSET,
            'v_offset': LCD.V_OFFSET,
            'gpio_LIGHT': LCD.GPIO_BACKLIGHT,
            'active_low': False,
            'bgr': True
        }

        super().__init__(serial_interface=interface, **params)


class Joystick():
    def __init__(self):
        self.up = gpiozero.Button(GPIO.JOY_UP)
        self.down = gpiozero.Button(GPIO.JOY_DOWN)
        self.left = gpiozero.Button(GPIO.JOY_LEFT)
        self.right = gpiozero.Button(GPIO.JOY_RIGHT)
        self.button = gpiozero.Button(GPIO.JOY_BUTTON)
        
    def get_direction(self) -> Tuple[int, int]:
        """Get x & y coordinates
        
        On a screen where top-left corner is (0, 0):
        
        - going left:  x_dir = -1
        - going right: x_dir = +1
        - going up:    y_dir = -1
        - going down:  y_dir = +1
        """
        x_dir = -self.left.is_pressed + self.right.is_pressed
        y_dir = -self.up.is_pressed + self.down.is_pressed
        
        return x_dir, y_dir


class Button(gpiozero.Button):
    def __init__(self, num: int):
        pins = [GPIO.KEY1, GPIO.KEY2, GPIO.KEY3]
        super().__init__(pins[num])


class Motor(gpiozero.DigitalOutputDevice):
    """Motor/relay combo set up as generic on/off output device"""
    def __init__(self):
        # map .on() to GPIO LOW
        super().__init__(GPIO.MOTOR, active_high=False)