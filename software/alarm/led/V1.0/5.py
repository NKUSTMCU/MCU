import RPi.GPIO as GPIO
import time
trigger_pin = 23
echo_pin = 24
led_pin = 26

trigger_pin1 = 31
echo_pin1 = 32
led_pin1 = 33

trigger_pin2 = 35
echo_pin2 = 36
led_pin2 = 37

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)


GPIO.setup(trigger_pin1, GPIO.OUT)
GPIO.setup(echo_pin1, GPIO.IN)


GPIO.setup(trigger_pin2, GPIO.OUT)
GPIO.setup(echo_pin2, GPIO.IN)


def send_trigger_pulse():
    GPIO.output(trigger_pin, True)
    time.sleep(0.001)
    GPIO.output(trigger_pin, False)

def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count - 1

def get_distance():
    send_trigger_pulse()
    wait_for_echo(True, 5000)
    start = time.time()
    wait_for_echo(False, 5000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len * 340 *100 /2
    distance_in = distance_cm / 2.5
    return (distance_cm, distance_in)
	
##1111111111111111111111111111111111111111111111111111111111111111111



def send_trigger_pulse1():
    GPIO.output(trigger_pin1, True)
    time.sleep(0.001)
    GPIO.output(trigger_pin1, False)

def wait_for_echo1(value, timeout):
    count = timeout
    while GPIO.input(echo_pin1) != value and count > 0:
        count = count - 1

def get_distance1():
    send_trigger_pulse1()
    wait_for_echo1(True, 5000)
    start = time.time()
    wait_for_echo1(False, 5000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm1 = pulse_len * 340 *100 /2
    distance_in1 = distance_cm1 / 2.5
    return (distance_cm1, distance_in1)
	
## 2222222222222222222222222222222222222222222222222222222222222222222



def send_trigger_pulse2():
    GPIO.output(trigger_pin2, True)
    time.sleep(0.001)
    GPIO.output(trigger_pin2, False)

def wait_for_echo2(value, timeout):
    count = timeout
    while GPIO.input(echo_pin2) != value and count > 0:
        count = count - 1

def get_distance2():
    send_trigger_pulse2()
    wait_for_echo2(True, 5000)
    start = time.time()
    wait_for_echo2(False, 5000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm2 = pulse_len * 340 *100 /2
    distance_in2 = distance_cm2 / 2.5
    return (distance_cm2, distance_in2)

while True:
    print("cm=%f\tinches=%f" % get_distance())
    print("cm=%f\tinches=%f" % get_distance1())
    print("cm=%f\tinches=%f" % get_distance2())
    time.sleep(1)
	
     if distance_cm<50:
         GPIO.output(led_pin, False)
         time.sleep(0.5)
         GPIO.output(led_pin, True)
         time.sleep(0.5)
     else:
          GPIO.output(led_pin, True)

	##11111111111111111111111111
	
	if distance_cm1<50:
           GPIO.output(led_pin1, False)
           time.sleep(0.5)
           GPIO.output(led_pin1, True)
           time.sleep(0.5)
     else:
          GPIO.output(led_pin1, True)
		  
	##2222222222222222222222222222
	
	if distance_cm2<50:
           GPIO.output(led_pin2, False)
           time.sleep(0.5)
           GPIO.output(led_pin2, True)
           time.sleep(0.5)
     else:
          GPIO.output(led_pin2, True)
		  
	
