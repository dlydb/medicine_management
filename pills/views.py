from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pins = [5,6,13,19,26]

for i in pins:
    GPIO.setup(i,GPIO.OUT)

def push(s, pins):
    GPIO.output(pins[s-1], GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pins[s-1], GPIO.LOW)
    time.sleep(0.1)

def dispenser(request):
    if 'S1' in request.POST:
        push(1, pins)
    elif 'S2' in request.POST:
        push(2, pins)
    elif 'S3' in request.POST:
        push(3, pins)
    elif 'S4' in request.POST:
        push(4, pins)
    elif 'S5' in request.POST:
        push(5, pins)
    return render(request,'control_page.html')
