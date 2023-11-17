from vex import *
import math

brain=Brain()
controller=Controller()
motorL=Motor(Ports.PORT1,GearSetting.RATIO_18_1,False)
motorR=Motor(Ports.PORT10,GearSetting.RATIO_18_1,True)

motorGroupL=MotorGroup(motorL)
motorGroupR=MotorGroup(motorR)

drivetrain=DriveTrain(motorGroupL,motorGroupR)

selectedPosition: bool=None
hasObject: bool=True
deadZone: int=10
inMotion: bool=False

def printToBrain(err):
   brain.screen.print('[ ' + str(brain.timer.time(TimeUnits.MSEC)) + ' ] ' + str(err))
   brain.screen.new_line()

def team_choosing():
   pass

def autonomous():
   drivetrain.set_stopping(BRAKE)

def driverControl():
   global selectedPosition, hasObject, selectedPosition, deadZone, inMotion

   while True:
      leftSpeed = 65*math.sin(0.007*controller.axis4.position())
      rightSpeed = 65*math.sin(0.007*controller.axis4.position())

      if leftSpeed < 3 and rightSpeed < -3:
         drivetrain.stop()
         inMotion = False
      else:
         inMotion = True
selectedPosition=team_choosing()

competition=Competition(driverControl, autonomous)