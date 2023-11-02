import vex
from vex import *

brain = vex.Brain()
controller = vex.Controller()
left_drive_motor = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
right_drive_motor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
arm_swing_motor = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO_18_1, False)
drivetrain = DriveTrain(left_drive_motor, right_drive_motor)

driver_control = False
field_position = None

def print_brain(process, msg='', typeIn):
    type = ''
    if typeIn.lower() == run:
        type = '[RUNNING]'
    if typeIn.lower() == fail:
        type = '[FAILED]'
    if typeIN.lower() == okay:
        type = '[OKAY]'
    brain.screen.print(STR(process.lower()).capitalize() + f' {type} ' + msg)
    brain.screen.new_line()

def launchElement():
    controller.rumble('-')
    arm_swing_motor.spin_for(vex.DirectionType.FORWARD, 5, vex.RotationUnits.DEG)
    arm_swing_motor.spin_for(vex.DirectionType.REVERSE, 5, vex.RotationUnits.DEG)

def handelElementUp():
    pass

def handelElementDown():
    pass

def Main():
    print_brain('Initialized',run,)
    print_brain('Initialized [OKAY]')

    def Autonomous():
        print_brain('Autonomous Routine [RUNNING]')

        class Positions:
            BLUE_RIGHT = 1
            BLUE_LEFT = 2
            RED_RIGHT = -1
            RED_LEFT = -2

        if Positions.BLUE_RIGHT == field_position:
            drivetrain.drive_for(vex.DirectionType.FORWARD, 1066, vex.DistanceUnits.MM)
            drivetrain.turn_for(vex.TurnType.LEFT, 90, vex.RotationUnits.DEG)
            launchElement()
            print_brain('Autonomous Routine [OKAY]: 1')

        elif Positions.BLUE_LEFT == field_position:
            drivetrain.drive_for(vex.DirectionType.FORWARD, 1066, vex.DistanceUnits.MM)
            drivetrain.turn_for(vex.TurnType.LEFT, 90, vex.RotationUnits.DEG)
            print_brain('Autonomous Routine [OKAY]: 2')

        elif Positions.RED_RIGHT == field_position:
            drivetrain.drive_for(vex.DirectionType.FORWARD, 1066, vex.DistanceUnits.MM)
            drivetrain.turn_for(vex.TurnType.LEFT, 90, vex.RotationUnits.DEG)
            print_brain('Autonomous Routine [OKAY]: -1')

        elif Positions.RED_LEFT == field_position:
            drivetrain.drive_for(vex.DirectionType.FORWARD, 1066, vex.DistanceUnits.MM)
            drivetrain.turn_for(vex.TurnType.LEFT, 90, vex.RotationUnits.DEG)
            launchElement()
            print_brain('-2','run')

        elif None == field_position:
            print_brain('Autonomous Routine [FAILED]: Error None Variable Value')
        else:
            print_brain('Autonomous Routine [FAILED]: Unknown Error')

    Autonomous()

    print_brain('Driver Control [RUNNING]')
    driver_control = True
    if driver_control == False:
        print_brain('Driver Control [FAILED]: Error Driver Control False')
    elif driver_control:
        print_brain('Driver Control [OKAY]')
    else:
        print_brain('Driver Control [FAILED]: Unknown Error')
    while driver_control:
        left_stick_y = controller.axis3.position()
        right_stick_x = controller.axis1.position()
        a = controller.buttonA.pressing()
        b = controller.buttonB.pressing()
        x = controller.buttonX.pressing()
        y = controller.buttonY.pressing()

        if left_stick_y != 0:
            left_drive_motor.spin(vex.DirectionType.FORWARD, left_stick_y, vex.VelocityUnits.PERCENT)
            right_drive_motor.spin(vex.DirectionType.FORWARD, left_stick_y, vex.VelocityUnits.PERCENT)
        else:
            left_drive_motor.stop()
            right_drive_motor.stop()

        if right_stick_x != 0:
            left_drive_motor.spin(vex.DirectionType.FORWARD, right_stick_x, vex.VelocityUnits.PERCENT)
            right_drive_motor.spin(vex.DirectionType.REVERSE, right_stick_x, vex.VelocityUnits.PERCENT)
        else:
            left_drive_motor.stop()
            right_drive_motor.stop()
        
        if a:
            launchElement()
        else:
            left_drive_motor.stop()
            right_drive_motor.stop()


        vex.wait(15)

Main()