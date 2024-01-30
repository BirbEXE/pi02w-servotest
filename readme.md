# Servo Test Script for Pi Zero 2 W

this script uses flask to generate a (very primative) webui for servo control via the Pi Zero 2 W.

The wiring requires that the data (PWM) pin of the servo is connected by default to GPIO 14, but this can be adjusted by changing line `11` of `main.py` to another GPIO value. Please note that not all GPIO pins support PWM control

for power, I have soldered the servo to the 5V debugging pin on the bottom of the Pi, and just used one of the ground pins for the servo.
please note: I do not reccomend this for long-term use and you should use a 5v power supply board if this is a permanent solution to prevent damaging your Pi02W.

for installation, just install flask via pip and this should run (if not pls open an issue)

read the docs here: https://gpiozero.readthedocs.io/en/stable/api_output.html#servo
