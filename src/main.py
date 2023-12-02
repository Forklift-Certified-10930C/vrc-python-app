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
isThrow=False
isTake=False

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
        if controller.buttonR1.pressing() and isThrow == False:
            motorGroupThrow.spin(FORWARD, 100, PERCENT)
        wait(20)

def onauton_autonomous_0():
    global selectedPosition
    if selectedPosition == 'blue_offence' or selectedPosition == 'red_offence':
        pass
    elif selectedPosition == 'blue_defence' or selectedPosition == 'red_defence':
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
    def team_choosing():
    while True:
        if controller_1.buttonL1.pressing():
            brain.screen.draw_image_from_file( "red_offence.png", 0, 4)
            while controller_1.buttonL1.pressing():
                wait(5, MSEC)
            return "red_offence"
        elif controller_1.buttonL2.pressing():
            brain.screen.draw_image_from_file( "red_defence.png", 0, 4)
            while controller_1.buttonL2.pressing():
                wait(5, MSEC)
            return "red_defence"
        elif controller_1.buttonR1.pressing():
            brain.screen.draw_image_from_file( "blue_offence.png", 0, 4)
            while controller_1.buttonR1.pressing():
                wait(5, MSEC)
            return "blue_offence"
        elif controller_1.buttonR2.pressing():
            brain.screen.draw_image_from_file( "blue_defence.png", 0, 4)
            while controller_1.buttonR2.pressing():
                wait(5, MSEC)
            return "blue_defence"

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