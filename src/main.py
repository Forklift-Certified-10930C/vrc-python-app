# Imports
import vex
from vex import *

# Parts
brain = vex.Brain()
controller = vex.Controller()
leftmotor = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
rightmotor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
drivetrain = vex.Drivetrain(leftmotor, rightmotor, gear_setting=vex.GEAR_RATIO_18, wheel_diameter=4.0, distance_units=vex.DIST_IN)

# Variables
drivercontrol = False
field_pos = None

# Functions
def print_brain(msg, color):
    brain.screen.set_font_color(color)
    brain.screen.print(msg)
    brain.screen.set_font_color(255, 255, 255)
    brain.screen.new_line()

# Main
def Main():
    print_brain('Initialized [RUNNING]', vex.colors.YELLOW)
    print_brain('Initialized [OKAY]', vex.colors.GREEN)
    print_brain('Starting Autonomous Routine [RUNNING]', vex.colors.YELLOW)
    
    async def Autonomous():
        if field_pos == 1:
            pass
        elif field_pos == 2:
            pass
        elif field_pos == -1:
            pass
        elif field_pos == -2:
            pass
        else:
            print_brain('Autonomous Routine [FAILED]', vex.colors.RED)
        print_brain('Autonomous Routine [OKAY]', vex.colors.GREEN)
    Autonomous()
    
    while drivercontrol:
        left_stick_y = controller.axis3.position()
        right_stick_x = controller.axis2.position()

        drivetrain.drive(left_stick_y, right_stick_x)

# Initalize
Main()