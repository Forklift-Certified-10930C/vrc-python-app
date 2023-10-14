import vex
from vex import *

brain = vex.Brain()
controller = vex.Controller()
leftmotor = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
rightmotor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
drivetrain = vex.Drivetrain(leftmotor, rightmotor, gear_setting=vex.GEAR_RATIO_18, wheel_diameter=4.0, distance_units=vex.DIST_IN)

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
        try:
            if field_position == 1:
                pass
            elif field_position == 2:
                pass
            elif field_position == -1:
                pass
            elif field_position == -2:
                pass
            elif field_position is None:
                raise ValueError(f'Autonomous Routine [FAILED]: Because of {field_position} value')
            else:
                raise ValueError('Autonomous Routine [FAILED]: Because of Unknown Error')
            print_brain('Autonomous Routine [OKAY]')
        except Exception as e:
            print_brain(str(e))
    drivercontrol = True

    Autonomous()

    while drivercontrol:
        left_stick_y = controller.axis3.position()
        right_stick_x = controller.axis2.position()

        drivetrain.drive(left_stick_y, right_stick_x)
Main()