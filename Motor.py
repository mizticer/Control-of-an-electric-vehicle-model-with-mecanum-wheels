import RPi.GPIO as GPIO

class Motor:
    def __init__(self, name, pwm_pin, in1, in2):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.name = name
        self.pwm_pin = pwm_pin
        self.in1 = in1
        self.in2 = in2
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        self.pwm = GPIO.PWM(self.pwm_pin, 1000)
        self.pwm.start(35)

motor_front_left = Motor( "front_left", 37, 29, 31)
motor_front_right = Motor("front_right", 11, 13, 15)
motor_back_left = Motor("back_left", 8, 10, 12)
motor_back_right = Motor("back_right", 22, 16, 18)
