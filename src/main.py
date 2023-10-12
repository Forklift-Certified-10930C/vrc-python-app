# Imports
import time
import vex
from vex import *

# Parts
brain = vex.Brain()
controller = vex.Controller()
motor_1 = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
motor_2 = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
drivetrain = Drivetrain(motor_1,motor_2)

# Variables


# Functions
def print_brain(msg):
    brain.screen.print(msg)
    brain.screen.new_line()

# Autonomous routine
def Autonomous():
    pass

Autonomous()
# Driver
def Main():
    print_brain('Initialized..')
    

Main()