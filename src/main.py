from vex import *
import time

brain=Brain()
controller=Controller()
left_drive_motor=Motor(Ports.PORT1,GearSetting.RATIO_18_1,False)
right_drive_motor=Motor(Ports.PORT10,GearSetting.RATIO_18_1,True)
drivetrain=DriveTrain(left_drive_motor,right_drive_motor)

starting_positions={
   "Blue": {
       "Right":1,
       "Left":2
   },
   "Red": {
       "Right":3,
       "Left":4
   }
}
driver_control=False
selected_position=None
haveObject=True
runTime=time.time()

def printToBrain(err):
   brain.screen.print('[ '+str(runTime) + ' ] '+str(err))
   brain.screen.new_line()

def autonomous():
   if starting_positions['Blue']['Right']==selected_position:
       return 0
   elif starting_positions['Blue']['Left']==selected_position:
       return 0
   elif starting_positions['Red']['Right']==selected_position:
       return 0
   elif starting_positions['Red']['Left']==selected_position:
       return 0
   elif selected_position==None:
       return 1
   else:
        return -1

printToBrain(autonomous())

while driver_control:
    a=controller.buttonA.pressed()
    b=controller.buttonB.pressed()
    x=controller.buttonX.pressed()
    y=controller.buttonY.pressed()

    up=controller.buttonUp.pressed()
    down=controller.buttonDown.pressed()
    left=controller.buttonLeft.pressed()
    right=controller.buttonRight.pressed()

    axis1=controller.axis1.position()
    axis2=controller.axis2.position()
    axis3=controller.axis3.position()
    axis4=controller.axis4.position()

    if axis1!=0:
        pass
    if axis2!=0:
        drivetrain.set_velocity(axis2,VelocityUnits.PERCENT)
    if axis3!=0:
        drivetrain.set_turn_velocity(axis3,VelocityUnits.PERCENT)
    if axis4!=0:
        pass
    else:
        drivetrain.stop()