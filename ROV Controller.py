from __future__ import division
from time import sleep
from guizero import App, PushButton, Slider, TextBox
from picamera import PiCamera
#import camstream
import Adafruit_PCA9685



        
pwm = Adafruit_PCA9685.PCA9685()

servo_right = 100  # Min pulse length out of 4096
servo_mid= 300
servo_left = 500 # Max pulse length out of 4096
servo_forward = 360
servo_stop = 400
servo_reverse = 420
servo_pumpon = 100
servo_pumptop = 500
servo_pumpoff = 100
servo_linear1 = 280
servo_linear2 = 0
servo_linear3 = 510

def slider_changed(slider_value):
    textbox.value = slider_value

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
def forward():
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, servo_forward)
    
def stop():
    pwm.set_pwm(0,0,servo_stop)

def reverse():
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, servo_reverse)

def right():
    # Move servo on channel O between extremes.
    pwm.set_pwm(3, 0, servo_right)
    
def neutral():
    pwm.set_pwm(3,0,servo_mid)

def left():
    # Move servo on channel O between extremes.
    pwm.set_pwm(3, 0, servo_left)
    
def pumpon():
    pwm.set_pwm(1,0,servo_pumpon)

def pumptop():
    pwm.set_pwm(1,0,servo_pumptop)
    pwm.set_pwm(2,0,servo_pumptop)
    
def pumpoff():
    pwm.set_pwm(2,0,servo_pumpoff)

def linearin():
    pwm.set_pwm(4,0,servo_linear1)
    
def linearmid():
    pwm.set_pwm(4,0,servo_linear2)

def linearout():
    pwm.set_pwm(4,0,servo_linear3)
    
def camera():
    camera = PiCamera()
    
    camera.resolution = (320, 240)
#camera.framerate = 25
    camera.framerate_range.high
    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    width = 10
    height = 10

app = App(title="ROV controller", height=400, width=400, layout="grid")

slider = Slider(app, start=280, end=510, command=slider_changed, grid=[6,3])
camera = PushButton(app, camera, text="Camera", grid=[3,4])
right = PushButton(app, right, text="Right", grid=[4,3])
neutral = PushButton(app, neutral, text="Neutral", grid=[3,3])
left = PushButton(app, left, text="Left", grid=[2,3])
forward= PushButton(app, forward, text="forward", grid=[3,0])
stop = PushButton(app, stop, text="stop", grid=[3,1])
reverse = PushButton(app, reverse, text="reverse", grid=[3,2])
pumpon = PushButton(app, pumpon, text="Pump In", grid=[2,5])
pumptop = PushButton(app, pumptop, text="Pump Stop", grid=[3,5])
pumpoff = PushButton(app, pumpoff, text="Pump Out", grid=[4,5])
linearin = PushButton(app, linearin, text="IN", grid=[2,6])
linearmid = PushButton(app, linearmid, text="MID", grid=[3,6])
linearout = PushButton(app, linearout, text="OUT", grid=[4,6])
textbox = TextBox(app, grid=[4,7])

app.display()


