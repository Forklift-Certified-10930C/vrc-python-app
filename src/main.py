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
        print_brain('Autonomous Routine [RUNNING]')
        try:
            BLUE_RIGHT = 1
            BLUE_LEFT = 2
            RED_RIGHT = -1
            RED_LEFT = -2

            switch_field_position = {
                BLUE_RIGHT: 'Autonomous Routine [OKAY]',
                BLUE_LEFT: 'Autonomous Routine [OKAY]',
                RED_RIGHT: 'Autonomous Routine [OKAY]',
                RED_LEFT: 'Autonomous Routine [OKAY]',
            }

            result = switch_field_position.get(field_position, None)
            if result is not None:
                print_brain(result)
            elif field_position is None:
                raise ValueError(f'Autonomous Routine [FAILED]: Because of {field_position} value')
            else:
                raise ValueError('Autonomous Routine [FAILED]: Because of Unknown Error')
        except Exception as e:
            print_brain(f'Autonomous Routine [FAILED]: Because {str(e)}')
        drivercontrol = True

    Autonomous()

    while drivercontrol:
        left_stick_y = controller.axis3.position()
        right_stick_x = controller.axis2.position()

        drivetrain.drive(vex.DirectionType.FWD, left_stick_y, vex.VelocityUnits.PCT)

Main()
