FROM python:3.8-buster

EXPOSE 80

RUN pip3 install Flask
RUN pip3 install adafruit-circuitpython-motorkit
RUN pip3 install RPi.GPIO

COPY /motor.py .
ENTRYPOINT ["python3", "motor.py"]