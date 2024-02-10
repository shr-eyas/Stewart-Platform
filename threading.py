import RPi.GPIO as GPIO
from time import sleep
import threading

class StepperMotor:
    def __init__(self, step_pin, dir_pin):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.speed = 500
        self.current_angle = 0
        self.current_steps = 0
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)

    def set_speed(self, new_speed):
        self.speed = new_speed

    def position(self, target_angle):
        target_steps = abs(target_angle / 0.1125)
        steps = int(target_steps - self.current_steps)

        GPIO.output(self.dir_pin, GPIO.HIGH if target_angle >= self.current_angle else GPIO.LOW)

        for _ in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            sleep(self.speed / 1000000.0)
            GPIO.output(self.step_pin, GPIO.LOW)
            sleep(self.speed / 1000000.0)

        self.current_angle = target_angle
        self.current_steps = target_steps

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Create instances for your motors
motor1 = StepperMotor(step_pin=17, dir_pin=18)
motor2 = StepperMotor(step_pin=22, dir_pin=23)
motor3 = StepperMotor(step_pin=22, dir_pin=23)
motor4 = StepperMotor(step_pin=22, dir_pin=23)
motor5 = StepperMotor(step_pin=22, dir_pin=23)
motor6 = StepperMotor(step_pin=22, dir_pin=23)
# Add more motors as needed

def move_motor(motor, target_angle):
    motor.position(target_angle)

theta1 = 360
theta2 = 360
theta3 = 360
theta4 = 360
theta5 = 360
theta6 = 360

# Start threads for each motor
thread1 = threading.Thread(target=move_motor, args=(motor1, theta1))
thread2 = threading.Thread(target=move_motor, args=(motor2, theta2))
thread3 = threading.Thread(target=move_motor, args=(motor3, theta3))
thread4 = threading.Thread(target=move_motor, args=(motor4, theta4))
thread5 = threading.Thread(target=move_motor, args=(motor5, theta5))
thread6 = threading.Thread(target=move_motor, args=(motor6, theta6))
# Add more threads for additional motors

# Start the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
# Start more threads as needed

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
# Join more threads as needed

# Clean up GPIO
GPIO.cleanup()
