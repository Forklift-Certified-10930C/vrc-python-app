import vex
from vex import *

brain = vex.Brain()
controller = vex.Controller()
leftmotor = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
rightmotor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(leftmotor, rightmotor)

drivercontrol = False
field_position = None

def print_brain(msg):
    brain.screen.print(msg)
    brain.screen.new_line()

def Main():
    print_brain('Initialized [RUNNING]')
    print_brain('Initialized [OKAY]')

def Autonomous():
    print_brain('Autonomous Routine [RUNNING]')

    class Positions:
        BLUE_RIGHT = 1
        BLUE_LEFT = 2
        RED_RIGHT = -1
        RED_LEFT = -2

    global field_position
    match field_position:
        case Positions.BLUE_RIGHT:
            print_brain('Autonomous Routine [OKAY]')

        case Positions.BLUE_LEFT:
            print_brain('Autonomous Routine [OKAY]')

        case Positions.RED_RIGHT:
            drivetrain.drive(vex.DirectionType.FORWARD, 1066)
            drivetrain.turn(vex.TurnType.RIGHT, 100, vex.VelocityUnits.PERCENT)
            print_brain('Autonomous Routine [OKAY]')

        case Positions.RED_LEFT:
            print_brain('Autonomous Routine [OKAY]')

        case None:
            print_brain('Autonomous Routine [FAILED]: None Variable Value')
        case _:
            print_brain('Autonomous Routine [FAILED]: Unknown Error')

    drivercontrol = True
    Autonomous()

    while drivercontrol:
        left_stick_y = controller.axis3.position()
        right_stick_x = controller.axis2.position()

        if left_stick_y > 0 or left_stick_y < 0:
            drivetrain.drive(vex.DirectionType.FORWARD, left_stick_y, vex.VelocityUnits.PERCENT)
        elif right_stick_x > 0 or right_stick_x < 0:
            drivetrain.turn(vex.TurnType.RIGHT, right_stick_x, vex.VelocityUnits.PERCENT)
        else:
            drivetrain.stop()

Main()