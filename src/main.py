import vex
from vex import *

brain = vex.Brain()
controller = vex.Controller()
leftmotor = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
rightmotor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(leftmotor, rightmotor)

drivercontrol = False
field_position = -1

def print_brain(msg):
    brain.screen.print(msg)
    brain.screen.new_line()

def Autonomous():
    print_brain('Autonomous Routine [RUNNING]')

    class Positions:
        BLUE_RIGHT = 1
        BLUE_LEFT = 2
        RED_RIGHT = -1
        RED_LEFT = -2

    if Positions.BLUE_RIGHT == field_position:
        print_brain('Autonomous Routine [OKAY]')

    elif Positions.BLUE_LEFT == field_position:
        print_brain('Autonomous Routine [OKAY]')

    elif Positions.RED_RIGHT == field_position:
        drivetrain.drive_for(vex.DirectionType.FORWARD, 1066, vex.DistanceUnits.MM)
        drivetrain.turn_for(vex.TurnType.RIGHT, 100, vex.RotationUnits.DEG)
        print_brain('Autonomous Routine [OKAY]')

    elif Positions.RED_LEFT == field_position:
        print_brain('Autonomous Routine [OKAY]')

    elif None == field_position:
        print_brain('Autonomous Routine [FAILED]: None Variable Value')
    else:
        print_brain('Autonomous Routine [FAILED]: Unknown Error')

    drivercontrol = True

def Main():
    print_brain('Initialized [RUNNING]')
    print_brain('Initialized [OKAY]')

    print_brain('Driver Control [RUNNING]')
    if drivercontrol != True:
        print_brain('Driver Control [OKAY]')
    while drivercontrol:
        left_stick_y = controller.axis3.position()
        right_stick_x = controller.axis1.position()

        if left_stick_y != 0:
            leftmotor.spin(vex.DirectionType.FORWARD, left_stick_y, vex.VelocityUnits.PERCENT)
            rightmotor.spin(vex.DirectionType.FORWARD, left_stick_y, vex.VelocityUnits.PERCENT)
        elif right_stick_x != 0:
            leftmotor.spin(vex.DirectionType.FORWARD, right_stick_x, vex.VelocityUnits.PERCENT)
            rightmotor.spin(vex.DirectionType.FORWARD, (right_stick_x * -1), vex.VelocityUnits.PERCENT)        
        else:
            leftmotor.stop()
            rightmotor.stop()
Main()