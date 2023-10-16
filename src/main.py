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
    
    BLUE_RIGHT = 1
    if field_position == BLUE_RIGHT:
        print_brain('Autonomous Routine [OKAY]')
        BLUE_LEFT = 2
    elif field_position == BLUE_LEFT:
        print_brain('Autonomous Routine [OKAY]')
    elif field_position == RED_RIGHT:
        print_brain('Autonomous Routine [OKAY]')
        RED_RIGHT = -1
    elif field_position == RED_LEFT:
        print_brain('Autonomous Routine [OKAY]')
        RED_LEFT = -2
    elif field_position is None:
        raise ValueError(f'Autonomous Routine [FAILED]: None Value')
    else:
        raise ValueError('Autonomous Routine [FAILED]: Unknown Error')

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
