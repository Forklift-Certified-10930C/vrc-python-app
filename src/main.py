from vex import *

brain=Brain()
controller=Controller()
motorL=Motor(Ports.PORT1,GearSetting.RATIO_18_1,False)
motorR=Motor(Ports.PORT10,GearSetting.RATIO_18_1,True)

motorGroupL=MotorGroup(motorL)
motorGroupR=MotorGroup(motorR)

driveTrain=DriveTrain(motorGroupL,motorGroupR)

selectedPosition: bool=None
haveObject: bool=True
deadZone: int=10

def printToBrain(err):
   brain.screen.print('[ ' + str(brain.timer.time(TimeUnits.MSEC)) + ' ] ' + str(err))
   brain.screen.new_line()

def chooseTeam():
   pass

def autonomous():
   pass

def driverControl():
   global selectedPosition, haveObject, selectedPosition, deadZone
   
   if controller.buttonA.pressing():
      pass
   else:
      if motorGroupR.is_spinning == False or motorGroupL.is_spining == False:
         driveTrain.stop()

selectedPosition=chooseTeam()

competition=Competition(driverControl, autonomous)