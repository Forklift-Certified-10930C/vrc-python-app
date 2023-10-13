# Imports
import vex
from vex import *

# Parts
brain = vex.Brain()
controller = vex.Controller()
leftmotor = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
rightmotor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
drive = vex.Drivetrain(leftmotor, rightmotor, gear_setting=vex.GEAR_RATIO_18, wheel_diameter=4.0, distance_units=vex.DIST_IN)

# Variables
drivercontrol = False

# Functions
def print_brain(msg):
    brain.screen.print(msg)
    brain.screen.new_line()

# Main
def Main():
    print_brain('Initialized..')
    
    while drivercontrol:
        left_stick_y = controller.axis2.position()
        right_stick_x = controller.axis1.position()

        drive.drive(left_stick_y, right_stick_x)

# Inits
Main()
