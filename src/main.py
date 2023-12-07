from vex import *
import random

brain=Brain()
controller=Controller(PRIMARY)
motorL=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motorR=Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
motorGroupL=MotorGroup(motorL)
motorGroupR=MotorGroup(motorR)
drivetrain=DriveTrain(motorGroupL, motorGroupR)
motorTop=Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
motorBottom=Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
throw=MotorGroup(motorTop, motorBottom)
motorFL=Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
motorFR=Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
intake=MotorGroup(motorFL, motorFR)
selectedPosition=True
hasObject=True
deadZone=10
inMotion=False
isSkill=False
isThrow=False
isTakeOut=False
isTakeIn=False

def ondriver_drivercontrol_0():
    global selectedPosition, hasObject, deadZone, inMotion, isSkill, isThrow, isTakeOut, isTakeIn
    while competition.is_enabled and competition.is_driver_control:
        if controller.axis1.position() > deadZone or controller.axis1.position() < -deadZone:
            drivetrain.turn(RIGHT, controller.axis1.position()*0.5, PERCENT)
            inMotion=True
        if controller.axis3.position() > deadZone or controller.axis3.position() < -deadZone:
            drivetrain.drive(FORWARD, controller.axis3.position(), PERCENT)
            inMotion=True
        if controller.axis3.position() == 0 and controller.axis1.position() == 0 and inMotion:
            drivetrain.stop()
            inMotion=False
        if controller.buttonA.pressing() and isThrow == False:
            throw.spin(REVERSE, 100, PERCENT)
            intake.spin(REVERSE, 100, PERCENT)
            isThrow=True
        if isThrow and controller.buttonA.pressing() == False:
            throw.stop()
            intake.stop()
            isThrow=False
        if controller.buttonR1.pressing() and isTakeOut == False:
            intake.spin(FORWARD, 100, PERCENT)
            isTakeOut=True
        if isTakeOut and controller.buttonR1.pressing() == False:
            intake.stop()
            isTakeOut=False
        if controller.buttonR2.pressing() and isTakeIn == False:
            intake.spin(REVERSE, 100, PERCENT)
            isTakeIn=True
        if isTakeIn and controller.buttonR2.pressing() == False:
            intake.stop()
            isTakeIn=False
        wait(20)

def onauton_autonomous_0():
    drivetrain.drive_for(FORWARD, 500, MM, 100, PERCENT)
    intake.__spin_for_time(REVERSE, 1000, MSEC, 100, PERCENT)
    drivetrain.drive_for(REVERSE, 550, MM, 100, PERCENT)

def printToBrain(func, err=0):
    if err == 0:
        brain.screen.print("[ {} ] No errors throw: at <{}>".format(brain.timer.time(MSEC), func))
        brain.screen.new_line()
    else:
        brain.screen.print("[ {} ] Error {}: at <{}>".format(brain.timer.time(MSEC), err, func))
        brain.screen.new_line()

def vexcode_auton_function():
    auton_task_0 = Thread( onauton_autonomous_0 )
    while( competition.is_autonomous() and competition.is_enabled() ):
        wait( 10, MSEC )
    auton_task_0.stop()

def vexcode_driver_function():
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    while( competition.is_driver_control() and competition.is_enabled() ):
        wait( 10, MSEC )
    driver_control_task_0.stop()


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )