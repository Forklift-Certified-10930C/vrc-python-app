# Imports
import random
import threading
import time
import vex
from vex import *

# Parts
brain = vex.Brain()
controller = vex.Controller()
motor_1 = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_36_1, False)
motor_2 = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO_36_1, False)

# Variables
right_stick_x = controller.axis1.position()
right_stick_y = controller.axis2.position()
left_stick_y = controller.axis3.position()
left_stick_x = controller.axis4.position()
is_A_pressed = controller.buttonA.pressing()
is_B_pressed = controller.buttonB.pressing()
is_Up_pressed = controller.buttonUp.pressing()
is_Down_pressed = controller.buttonDown.pressing()
is_Left_pressed = controller.buttonLeft.pressing()
is_Right_pressed = controller.buttonRight.pressing()
field_pos = None

# Functions
def motor1(rpm):
    motor_1.spin(vex.DirectionType.FORWARD, rpm, vex.VelocityUnits.RPM)

def motor2(rpm):
    motor_2.spin(vex.DirectionType.FORWARD, rpm, vex.VelocityUnits.RPM)

def get_pos():
       while field_pos == None:
        if is_Up_pressed:
            return 1
        elif is_Right_pressed:
            return 2
        elif is_Down_pressed:
            return -1
        elif is_Left_pressed:
            return -2


# Main
brain.screen.print('Initialized...')

# Autonomous routine
field_pos = get_pos()

if field_pos == 1:
    pass
if field_pos == 2:
    pass
if field_pos == -1:
    pass
if field_pos == -2:
    pass

# Driver
while True:

    motor1(left_stick_y)
    motor2(right_stick_x)