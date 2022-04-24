# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File:         movement.py
# Created By:   Adrian Mysak
# Year:         2022
# Major V.:     1
"""
Library to access motor driver of 'Maze Robot'
"""


from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep
from board import I2C

import atexit


class MRMovement:
    def __init__(self, field_size=1):
        self._filed_size = field_size
        self._kit = MotorKit(i2c=I2C())
        self._step1 = self._kit.stepper1
        self._step2 = self._kit.stepper2

    def _move_forward(self, type='step', steps=1):
        types = ['step', 'field']
        if type not in types:
            raise ValueError("Invalid Type: {type}, please use one of those: {types}".format(
                type=type, types=types))

        if type == 'step':
            for i in range(steps):
                self._step1.onestep(
                    direction=stepper.BACKWARD, style=stepper.DOUBLE)
                self._step2.onestep(
                    direction=stepper.BACKWARD, style=stepper.DOUBLE)
                sleep(.03)
            self._step1.release()
            self._step2.release()

        elif type == 'field':
            print("field is currently not supported.")

    def _move_backward(self, type='step', steps=1):
        types = ['step', 'field']
        if type not in types:
            raise ValueError("Invalid Type: {type}, please use one of those: {types}".format(
                type=type, types=types))

        if type == 'step':
            for i in range(steps):
                self._step1.onestep(
                    direction=stepper.BACKWARD, style=stepper.DOUBLE)
                self._step2.onestep(
                    direction=stepper.BACKWARD, style=stepper.DOUBLE)
                sleep(.03)
            self._step1.release()
            self._step2.release()

        elif type == 'field':
            print("field is currently not supported.")

    def exit_handler(self):
        print("Stopping app, releasing motors if necessary.")
        self._step1.release()
        self._step2.release()


atexit.register(MRMovement().exit_handler)
