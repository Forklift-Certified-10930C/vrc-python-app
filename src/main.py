import vex
from vex import *

brain = vex.Brain()
controller = vex.Controller()
left_drive_motor = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
right_drive_motor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
arm_swing_motor = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO_18_1, False)
drivetrain = DriveTrain(left_drive_motor, right_drive_motor)

driver_control = False
field_position = -1

def print_brain(msg):
    brain.screen.print(msg)
    brain.screen.new_line()

def launchElement():
    pass

def handelElementUp():
    pass

def handelElementDown():
    pass

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
            print_brain('Autonomous Routine [FAILED]: Error None Variable Value')
        else:
            print_brain('Autonomous Routine [FAILED]: Unknown Error')

        driver_control = True

    Autonomous()

    print_brain('Driver Control [RUNNING]')
    if bool(driver_control):
        print_brain(f'Driver Control [FAILED]: Error {driver_control} Variable Value')
    elif driver_control:
        print_brain('Driver Control [OKAY]')
    else:
        print_brain(f'Driver Control [FAILED]: Unknown Error')
    while driver_control:
        left_stick_y = controller.axis3.position()
        right_stick_x = controller.axis1.position()

        if left_stick_y != 0:
            left_drive_motor.spin(vex.DirectionType.FORWARD, left_stick_y, vex.VelocityUnits.PERCENT)
            right_drive_motor.spin(vex.DirectionType.FORWARD, left_stick_y, vex.VelocityUnits.PERCENT)
        elif right_stick_x != 0:
            left_drive_motor.spin(vex.DirectionType.FORWARD, right_stick_x, vex.VelocityUnits.PERCENT)
            right_drive_motor.spin(vex.DirectionType.REVERSE, right_stick_x, vex.VelocityUnits.PERCENT)        
        else:
            left_drive_motor.stop()
            right_drive_motor.stop()

Main()