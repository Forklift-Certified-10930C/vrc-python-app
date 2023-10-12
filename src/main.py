# Imports
import time
import vex
from vex import *

# Parts
brain = vex.Brain()
controller = vex.Controller()
motor_1 = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
motor_2 = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
drivetrain1 = Drivetrain(motor_1,motor_2)

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
def print_brain(msg):
    brain.screen.print(msg)
    brain.screen.new_line()

def drive_forward(vel):
    drivetrain1(FORWARD, vel, )

# Main
print_brain('Initialized..')
# Autonomous routine

# Driver