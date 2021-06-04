from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from flask import Flask, request
import sys
import time

kit = MotorKit()
kit.motor1.throttle = 1.0
time.sleep(5)
kit.motor1.throttle = 0
