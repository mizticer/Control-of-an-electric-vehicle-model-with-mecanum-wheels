import time

class PID:
    def __init__(self , Kp=0, Ki=0, Kd=0, setpoint =0,
        windup_max =0):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.windup_max = windup_max
        self.PID_output = 0
        self.last_time = time.time ()
        self.last_error = 0
        self.P = 0
        self.I = 0
        self.D = 0
    def calculate(self , feedback):
        error = self.setpoint - feedback
        dt = time.time() - self.last_time
        de = error - self.last_error
        self.P = error
        self.I += error * dt
        self.I = max(min(self.I, self.windup_max), -self.windup_max)
        self.D =  de / dt
        self.last_error = error
        self.last_time = time.time()
        self.PID_output =  max(min(50,self.Kp * self.P + self.Ki * self.I + self.Kd * self.D), -50)
        print("output from regulator [%s]" %self.PID_output)
    def clear(self):
        self.PID_output = 0
        self.last_error = 0
        self.I= 0
        
pid = PID(Kp = 0.45, Ki = 0.3, windup_max = 2)

        
