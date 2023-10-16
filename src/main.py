import vex
from vex import *

brain = vex.Brain()
controller = vex.Controller()
leftmotor = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
rightmotor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
drivetrain = vex.Drivetrain(leftmotor, rightmotor)

drivercontrol = False
field_position = None

def print_brain(msg):
    brain.screen.print(msg)
    brain.screen.new_line()

def Main():
    print_brain('Initialized [RUNNING]')
    print_brain('Initialized [OKAY]')

async def Autonomous():
    print_brain('Autonomous Routine [RUNNING]')
    class Positions:
        BLUE_RIGHT = 1
        BLUE_LEFT = 2
        RED_RIGHT = -1
        RED_LEFT = -2

    match field_position:
        case Positions.BLUE_RIGHT:
            print_brain('Autonomous Routine [OKAY]')
        case Positions.BLUE_LEFT:
            print_brain('Autonomous Routine [OKAY]')
        case Positions.RED_RIGHT:
            print_brain('Autonomous Routine [OKAY]')
        case Positions.RED_LEFT:
            print_brain('Autonomous Routine [OKAY]')
        case _:
            print_brain('Autonomous Routine [FAILED]: None Variable')


try:
    drivercontrol = True
    Autonomous()

    while drivercontrol:
        left_stick_y = controller.axis3.position()
        right_stick_x = controller.axis2.position()

        drivetrain.drive(vex.DirectionType.FWD, left_stick_y, vex.VelocityUnits.PCT)
except Exception as e:
    print_brain(f'Driver Control [FAILED]: {str(e)}')

Main()
