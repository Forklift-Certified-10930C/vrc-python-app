from vex import *

brain=Brain()
controller=Controller()
motorL=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motorR=Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
motorGroupL=MotorGroup(motorL)
motorGroupR=MotorGroup(motorR)
drivetrain=DriveTrain(motorGroupL, motorGroupR)
motorTop=Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
motorBottom=Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
motorGroupThrow=MotorGroup(motorTop, motorBottom)
motorFL=Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
motorFR=Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
frontMotorGroup=MotorGroup(motorFL, motorFR)
selectedPosition=True
hasObject=True
deadZone=10
inMotion=False
isSkill=False
throwToggle=False
reverse=1

def ondriver_drivercontrol_0():
    global selectedPosition, hasObject, deadZone, inMotion, isSkill, throwToggle, reverse
    while competition.is_enabled and competition.is_driver_control:
        if controller.axis1.position() > deadZone or controller.axis1.position() < -deadZone:
            drivetrain.turn(RIGHT, controller.axis1.position(), PERCENT)
            inMotion=True
        if controller.axis3.position() > deadZone or controller.axis3.position() < -deadZone:
            drivetrain.drive(FORWARD, controller.axis3.position(), PERCENT)
            inMotion=True
        if controller.axis3.position() == 0 and controller.axis1.position() == 0 and inMotion:
            drivetrain.stop()
            inMotion=False
        if controller.buttonLeft.pressing():
            drivetrain.set_stopping(COAST)
        if controller.buttonRight.pressing():
            drivetrain.set_stopping(BRAKE)
        if controller.buttonR1.pressing() and True:
            pass
        wait(20)

def onauton_autonomous_0():
    global selectedPosition
    if selectedPosition == 'Blue Offence' or selectedPosition == 'Red Defence':
        pass
    elif selectedPosition == 'Blue Defence' or selectedPosition == 'Red Defence':
        pass
    elif selectedPosition == 'skill':
        pass

def printToBrain(err, func):
    if err == 0:
        brain.screen.print("[ {} ] No errors throw: at <{}>".format(brain.timer.time(MSEC), func))
        brain.screen.new_line()
    else:
        brain.screen.print("[ {} ] Error {}: at <{}>".format(brain.timer.time(MSEC), err, func))
        brain.screen.new_line()

def chooseTeam():
    while selectedPosition:
        if controller.buttonR1.pressing():
            pass

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
selectedPosition = chooseTeam()
competition = Competition( vexcode_driver_function, vexcode_auton_function )