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
   elif starting_positions['Blue']['Left'] == selected_position:
       return 0
   elif starting_positions['Red']['Right'] == selected_position:
       return 0
   elif starting_positions['Red']['Left'] == selected_position:
       return 0
   elif selected_position == None:
       return 1
   else:
        return -1

def main():
    return 0

printToBrain(autonomous())
printToBrain(main())