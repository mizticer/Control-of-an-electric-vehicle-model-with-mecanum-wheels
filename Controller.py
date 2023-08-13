import Directions
import Motor
import Speed
from PID import pid
from time import sleep

def follow_line(error,detected_route):
    pid.calculate(error)
    if detected_route!=0:
        Directions.forward()
        if error<=0 and error>=-100: 
            Motor.motor_front_right.pwm.ChangeDutyCycle(35+int(pid.PID_output))
            Motor.motor_front_left.pwm.ChangeDutyCycle(35)
            Motor.motor_back_right.pwm.ChangeDutyCycle(35)
            Motor.motor_back_left.pwm.ChangeDutyCycle(35+int(pid.PID_output))
            print("w lewo")
        if error>=0 and error<=100: 
            print("w prawo")
            Motor.motor_front_right.pwm.ChangeDutyCycle(35)
            Motor.motor_front_left.pwm.ChangeDutyCycle(35-int(pid.PID_output))
            Motor.motor_back_right.pwm.ChangeDutyCycle(35-int(pid.PID_output))
            Motor.motor_back_left.pwm.ChangeDutyCycle(35)
        if error>100:
            Directions.right_around()
            Speed.speed_of_motor(25-int(pid.PID_output))
        if error<-100:
            Directions.left_around()
            Speed.speed_of_motor(25+int(pid.PID_output))
    else:   
        Directions.stop()
        Speed.speed_of_motor(0)
        pid.clear()
       

   