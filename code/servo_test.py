import logging
import time

from utils import devices

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    servo = devices.Servo(0)

    servo.min()
    time.sleep(2)

    servo.max()
    time.sleep(2)

    servo.value = .5
    time.sleep(2)