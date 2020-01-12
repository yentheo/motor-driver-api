from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from flask import Flask, request
import sys

kit = MotorKit()

app = Flask(__name__)


@app.route('/')
def rotate():
    degrees = int(request.args.get('degrees'), 10)

    for i in range(int(degrees / 0.9)):
        kit.stepper1.onestep(style=stepper.DOUBLE)
        
    kit.stepper1.release()

if __name__ == '__main__':
    app.run(host= '0.0.0.0')