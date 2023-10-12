# Imports
from vex import *

# Parts
brain = Brain()
controller = Controller()
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_2 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
drivetrain = Drivetrain(motor_1,motor_2)

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
        drivetrain.drive(FORWARD, controller.axis3.position(), PERCENT)
        drivetrain.turn(RIGHT, controller.axis4.position(), PERCENT)

# Inits
Main()