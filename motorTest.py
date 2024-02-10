import RPi.GPIO as GPIO
from time import sleep

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins for the stepper motor
step_pin = 17
dir_pin = 18

# Set up the GPIO pins
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)

# Set the initial direction (1 for clockwise, 0 for counterclockwise)
direction = 1

# Set the initial speed
speed = 500  # microseconds per step

# Run the stepper motor
try:
    # Move 200 steps clockwise
    GPIO.output(dir_pin, direction)
    for _ in range(200):
        GPIO.output(step_pin, GPIO.HIGH)
        sleep(speed / 1000000.0)
        GPIO.output(step_pin, GPIO.LOW)
        sleep(speed / 1000000.0)
    sleep(1)

    # Move 200 steps counterclockwise
    GPIO.output(dir_pin, !direction)
    for _ in range(200):
        GPIO.output(step_pin, GPIO.HIGH)
        sleep(speed / 1000000.0)
        GPIO.output(step_pin, GPIO.LOW)
        sleep(speed / 1000000.0)
    sleep(1)

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO
    GPIO.cleanup()
