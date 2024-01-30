#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import time
from urllib.request import urlopen
from flask import Flask, request, render_template, redirect, url_for

# import servo libraries
from gpiozero import Servo

servo = Servo(14)

try:
    app = Flask(__name__)

    @app.route('/')
    def my_form():
        return render_template('servo.html')

    @app.route('/', methods=['POST'])
    def my_form_post():
        angle = request.form.get('angle')
        action = request.form.get('action')
        submit_button = request.form.get('submit')

        if action == 'Max':
            print("max")
            servo.max()
        elif action == 'Center':
            print("center")
            servo.mid()
        elif action == 'Min':
            print("min")
            servo.min()
        elif submit_button == 'Submit':
            print(f"Submit angle: {angle}")
            servo.value = angle
        else:
            print("else???")

        return redirect(url_for('my_form'))

    app.run(port=8000, host="0.0.0.0")

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    exit()