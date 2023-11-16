from vex import *

brain=Brain()
controller=Controller()
motorA=Motor(Ports.PORT1,GearSetting.RATIO_18_1,False)
motorB=Motor(Ports.PORT10,GearSetting.RATIO_18_1,True)
drivetrain=DriveTrain(motorA,motorB)

selectedPosition=None
haveObject=True
startTime=time.time()
deadZone=10

def printToBrain(err):
   brain.screen.print('[ ' + str(brain.timer.time(TimeUnits.MSEC)) + ' ] ' + str(err))
   brain.screen.new_line()

def team_choosing():
   pass

def autonomous():
   pass

def driver_control():
   global selectedPosition, haveObject, selectedPosition, deadZone

selectedPosition = team_choosing()

competition = Competition(driver_control, autonomous)