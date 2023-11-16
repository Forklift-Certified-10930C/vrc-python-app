from vex import *

brain=Brain()
controller=Controller()
left_drive_motor=Motor(Ports.PORT1,GearSetting.RATIO_18_1,False)
right_drive_motor=Motor(Ports.PORT10,GearSetting.RATIO_18_1,True)
drivetrain=DriveTrain(left_drive_motor,right_drive_motor)

selected_position=None
haveObject=True
start_time=time.time()

def printToBrain(err):
   brain.screen.print('[ ' + str(brain.timer.time(TimeUnits.MSEC)) + ' ] ' + str(err))
   brain.screen.new_line()

def team_choosing():
    pass

def autonomous():
   pass

def driver_control():
    global selected_position, haveObject, selected_position
    pass

selected_position = team_choosing()

competition = Competition(driver_control, autonomous)