import Motor

def speed_of_motor(data):
    Motor.motor_front_right.pwm.ChangeDutyCycle(max(min(100,int(data)), 0))
    Motor.motor_front_left.pwm.ChangeDutyCycle(max(min(100,int(data)), 0))
    Motor.motor_back_right.pwm.ChangeDutyCycle(max(min(100,int(data)), 0))
    Motor.motor_back_left.pwm.ChangeDutyCycle(max(min(100,int(data)), 0))
    

    