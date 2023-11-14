if False:
    pass
    # def print_brain(typeIn: str, process: str, ErrorMessage=': ',):

    #     LogType = ''
    #     if typeIn.lower() == 'run':
    #         LogType = '[RUNNING]'
    #     if typeIn.lower() == 'fail':
    #         LogType = '[FAILED]'
    #     if typeIn.lower() == 'okay' or "ok":
    #         LogType = '[OKAY]'

    #     printItem = (process.lower()).capitalize() + LogType + ErrorMessage.upper()

    #     brain.screen.print(printItem)
    #     brain.screen.new_line()

    # def launchElement():
    #     controller.rumble('.')

    # def handelElementUp():
    #     HoldingItem = True

    # def handelElementDown():
    #     HoldingItem = False

    # def main():
    #     print_brain('run', 'Initialized')
    #     print_brain('OKAY', 'Initialized')

    #     def Autonomous():
    #         print_brain('RUNNING', 'Autonomous Routine')

    #         class Positions:
    #             BLUE_RIGHT = 1
    #             BLUE_LEFT = 2
    #             RED_RIGHT = -1
    #             RED_LEFT = -2

    #         if Positions.BLUE_RIGHT == field_position:
    #             drivetrain.drive_for(vex.DirectionType.FORWARD, 1066, vex.DistanceUnits.MM)
    #             drivetrain.turn_for(vex.TurnType.LEFT, 90, vex.RotationUnits.DEG)
    #             launchElement()
    #             print_brain('okay', 'Autonomous Routine', '1')

    #         elif Positions.BLUE_LEFT == field_position:
    #             drivetrain.drive_for(vex.DirectionType.FORWARD, 1066, vex.DistanceUnits.MM)
    #             drivetrain.turn_for(vex.TurnType.LEFT, 90, vex.RotationUnits.DEG)
    #             print_brain('okay', 'Autonomous Routine', '2')

    #         elif Positions.RED_RIGHT == field_position:
    #             drivetrain.drive_for(vex.DirectionType.FORWARD, 1066, vex.DistanceUnits.MM)
    #             drivetrain.turn_for(vex.TurnType.LEFT, 90, vex.RotationUnits.DEG)
    #             print_brain('okay', 'Autonomous Routine', '-1')

    #         elif Positions.RED_LEFT == field_position:
    #             drivetrain.drive_for(vex.DirectionType.FORWARD, 1066, vex.DistanceUnits.MM)
    #             drivetrain.turn_for(vex.TurnType.LEFT, 90, vex.RotationUnits.DEG)
    #             launchElement()
    #             print_brain('okay', 'Autonomous Routine', '-2')

    #         elif None == field_position:
    #             print_brain('fail', 'Autonomous Routine', 'ERR_None')
    #         else:
    #             print_brain('fail', 'Autonomous Routine', 'ERR_UNKOWN')

    #     Autonomous()

    #     print_brain('run', 'driver control')
    #     driver_control = True
    #     if driver_control == False:
    #         print_brain('fail', 'driver control', 'ERR_FALSE')
    #     elif driver_control:
    #         print_brain('okay', 'driver control')
    #     else:
    #         print_brain('fail', 'driver control', 'ERR_UNKOWN')
    #     while driver_control:
    #         left_stick_y = controller.axis3.position()
    #         right_stick_x = controller.axis1.position()
    #         a = controller.buttonA.pressing()
    #         b = controller.buttonB.pressing()
    #         x = controller.buttonX.pressing()
    #         y = controller.buttonY.pressing()

    #         if left_stick_y != 0:
    #             left_drive_motor.spin(vex.DirectionType.FORWARD, left_stick_y, vex.VelocityUnits.PERCENT)
    #             right_drive_motor.spin(vex.DirectionType.FORWARD, left_stick_y, vex.VelocityUnits.PERCENT)
    #         else:
    #             left_drive_motor.stop()
    #             right_drive_motor.stop()
    #         if right_stick_x != 0:
    #             left_drive_motor.spin(vex.DirectionType.FORWARD, right_stick_x, vex.VelocityUnits.PERCENT)
    #             right_drive_motor.spin(vex.DirectionType.REVERSE, right_stick_x, vex.VelocityUnits.PERCENT)
    #         else:
    #             left_drive_motor.stop()
    #             right_drive_motor.stop()

    #         if a:
    #             launchElement()
    #         if b:
    #             if HoldingItem:
    #                 handelElementDown()
    #             else:
    #                 handelElementUp()
    #         if x:
    #             pass
    #         if y:
    #             pass

    #         vex.wait(15)
    # main()

from vex import *
import time

brain = Brain()
controller = Controller()
left_drive_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_drive_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_motor, right_drive_motor)

starting_positions = {
   "Blue": {
       "Right": 1,
       "Left": 2
   },
   "Red": {
       "Right": 3,
       "Left": 4
   }
}
selected_position = None
haveObject = True
runTime = time.time()

def printToBrain(err):
   message = '[ ' + str(runTime) + ' ] ' + str(err)
   brain.screen.print(message)
   brain.screen.new_line()

def autonomous():
   if starting_positions['Blue']['Right'] == selected_position:
       return 0
   if starting_positions['Blue']['Left'] == selected_position:
       return 0
   if starting_positions['Red']['Right'] == selected_position:
       return 0
   if starting_positions['Red']['Left'] == selected_position:
       return 0
   else:
        return 1

printToBrain(autonomous())