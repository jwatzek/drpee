import gpiozero

# read motor/relay setup as generic on/off output device
# start in off position; set so that .on() sets GPIO to LOW
motor = gpiozero.DigitalOutputDevice(23,
                                     active_high=False,
                                     initial_value=False)

# make it go :D
motor.blink(on_time=2, off_time=5, n=3)
