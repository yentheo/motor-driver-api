from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from flask import Flask, request
import time
import sys

kit = MotorKit()

app = Flask(__name__)

isUp = True

@app.route('/move')
def move():
    direction = 1 if request.args.get('direction') == 'up' else -1
    length = 40 if request.args.get('length') is None else int(request.args.get('length'))
    kit.motor1.throttle = direction
    time.sleep(length / 2.3)
    kit.motor1.throttle = 0
    return 'turned\n'

@app.route('/toggle')
def toggle():
    global isUp
    direction = -1 if isUp else 1
    kit.motor1.throttle = direction
    time.sleep(20)
    kit.motor1.throttle = 0
    isUp = not isUp
    return 'turned'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
