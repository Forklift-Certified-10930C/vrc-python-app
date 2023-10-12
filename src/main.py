# Imports
import vex

# Parts
brain = vex.Brain()
controller = vex.Controller()
motor_1 = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_18_1, False)
motor_2 = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)
drivetrain = vex.Drivetrain(motor_1,motor_2)

# Variables
drivercontrol = False

# Functions
def print_brain(msg):
    brain.screen.print(msg)
    brain.screen.new_line()

# Main
def Main():
    print_brain('Initialized..')
    
    while drivercontrol:
        left_stick_y = controller.axis2.position()
        right_stick_x = controller.axis1.position()

        left_speed = left_stick_y + right_stick_x
        right_speed = left_stick_y - right_stick_x

        drivetrain.set_drive_velocity(left_speed, vex.VelocityUnits.PERCENT)
        drivetrain.set_turn_velocity(right_speed, vex.VelocityUnits.PERCENT)

# Inits
Main()
