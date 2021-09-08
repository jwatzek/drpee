import logging
import time

from utils import devices

pir = devices.MotionSensor()

counter = 0

while True:
    _ = pir.wait_for_motion()
    start = time.time()
    counter += 1
    print('motion detected!', counter)
    
    _ = pir.wait_for_no_motion()
    print('motion stopped :(', time.time() - start)
    print()
    
    