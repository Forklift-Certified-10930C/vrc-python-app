from vex import *
import math

brain=Brain()
controller=Controller()
motorL=Motor(Ports.PORT1,GearSetting.RATIO_18_1,False)
motorR=Motor(Ports.PORT10,GearSetting.RATIO_18_1,True)

motorGroupL=MotorGroup(motorL)
motorGroupR=MotorGroup(motorR)

drivetrain=DriveTrain(motorGroupL,motorGroupR)

selectedPosition=None
hasObject: bool=True
deadZone: int=10
inMotion: bool=False

def printToBrain(err):
   brain.screen.print('[ ' + str(brain.timer.time(TimeUnits.MSEC)) + ' ] ' + str(err))
   brain.screen.new_line()
def handelObject():
   if hasObject:
      return 'WIP'
   else:
      return 'WIP'
def throwobject():
   if hasObject:
      return 1
   else:
      return 'WIP'
def team_choosing():
   while selectedPosition == None:
      if controller.buttonL1.pressing():
         return 'Red Offence'
      if controller.buttonL2.pressing():
         return 'Red Defence'
      if controller.buttonR1.pressing():
         return 'Blue Offence'
      if controller.buttonR2.pressing():
         return 'Blue Defence'
      wait(20)
def autonomous():
   global selectedPosition
   drivetrain.set_stopping(BRAKE)
   if selectedPosition == 'Red Offence' or selectedPosition == 'Blue Offence':
      drivetrain.drive_for(FORWARD, 1800, MM)
      drivetrain.turn_for(LEFT, 90, DEGREES)
      drivetrain.drive_for(FORWARD, 500 ,MM)
      printToBrain(handelObject())
      return 0
   if selectedPosition == 'Red Defence' or selectedPosition == 'Blue Defence':
      drivetrain.drive_for(FORWARD, 1000, MM)
      drivetrain.turn_for(RIGHT, 90, DEGREES)
      return 0
def driverControl():
   global selectedPosition, hasObject, selectedPosition, deadZone, inMotion

   while True:
      if inMotion != 0:
         inMotion = True
      if controller.buttonUp.pressing():
         drivetrain.set_stopping(COAST)
      if controller.buttonDown.pressing():
         drivetrain.set_stopping(BRAKE)
      if controller.buttonA.pressing():
         drivetrain.stop()
         inMotion = False
      if controller.axis3.position != 0:
         drivetrain.drive(FORWARD, controller.axis3.position(), PERCENT)
      if controller.axis1.position != 0:
         drivetrain.turn(FORWARD, controller.axis1.position(), PERCENT)

   

selectedPosition=team_choosing()