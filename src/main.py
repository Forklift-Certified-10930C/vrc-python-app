import vex
from vex import *

brain = vex.Brain()
controller = vex.Controller()
leftmotor = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
rightmotor = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
drivetrain = vex.Drivetrain(leftmotor, rightmotor, gear_setting=vex.GEAR_RATIO_18, wheel_diameter=4.0, distance_units=vex.DIST_IN)

drivercontrol = False
field_pos = None

def print_brain(msg):
    if '[RUNNING]' in msg:
        brain.screen.set_font_color(vex.colors.YELLOW)
        brain.screen.print(msg)
        brain.screen.set_font_color(255, 255, 255)
        brain.screen.new_line()
    elif '[OKAY]' in msg:
        brain.screen.set_font_color(vex.colors.GREEN)
        brain.screen.print(msg)
        brain.screen.set_font_color(255, 255, 255)
        brain.screen.new_line()
    elif '[FAILED]' in msg:
        brain.screen.set_font_color(vex.colors.RED)
        brain.screen.print(msg)
        brain.screen.set_font_color(255, 255, 255)
        brain.screen.new_line()
    else:
        brain.screen.print(msg)
        brain.screen.set_font_color(255, 255, 255)
        brain.screen.new_line()

def Main():
    print_brain('Initialized [RUNNING]')
    print_brain('Initialized [OKAY]')

    async def Autonomous():
        print_brain('Autonomous Routine [RUNNING]')
        try:
            if field_pos == 1:
                pass
            elif field_pos == 2:
                pass
            elif field_pos == -1:
                pass
            elif field_pos == -2:
                pass
            elif field_pos is None:
                raise ValueError(f'Autonomous Routine [FAILED]: Because of {field_pos} value')
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