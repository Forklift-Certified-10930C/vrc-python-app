from vex import *
import math

PETER_GRIFFN=Brain()
GPS=Gps(Ports.PORT22)
CONTROLLER=Controller(PRIMARY)
MOTOR_1=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
MOTOR_2=Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
MOTOR_GROUP_L=MotorGroup(MOTOR_1)
MOTOR_GROUP_R=MotorGroup(MOTOR_2)
DRIVETRAIN=DriveTrain(MOTOR_GROUP_L, MOTOR_GROUP_R)
MOTOR_7=Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
MOTOR_5=Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
MOTOR_GROUP_THROW=MotorGroup(MOTOR_7, MOTOR_5)
MOTOR_3=Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
MOTOR_8=Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
MOTOR_GROUP_INTAKE=MotorGroup(MOTOR_3, MOTOR_8)
HAS_OBJ=True
DEAD_ZONE=10
IN_MOTION=False
isSkill=False
IS_THROW=False
IS_TAKE_OUT=False
IS_TAKE_IN=False

def ondriver_drivercontrol_0():
    global HAS_OBJ, DEAD_ZONE, IN_MOTION, isSkill, IS_THROW, IS_TAKE_OUT, IS_TAKE_IN
    while competition.is_enabled and competition.is_driver_control:
        if CONTROLLER.axis1.position() > DEAD_ZONE or CONTROLLER.axis1.position() < -DEAD_ZONE:
            DRIVETRAIN.turn(RIGHT, CONTROLLER.axis1.position()*0.5, PERCENT)
            IN_MOTION=True
        if CONTROLLER.axis3.position() > DEAD_ZONE or CONTROLLER.axis3.position() < -DEAD_ZONE:
            DRIVETRAIN.drive(FORWARD, CONTROLLER.axis3.position(), PERCENT)
            IN_MOTION=True
        if CONTROLLER.axis3.position() == 0 and CONTROLLER.axis1.position() == 0 and IN_MOTION:
            DRIVETRAIN.stop()
            IN_MOTION=False
        if CONTROLLER.buttonA.pressing() and IS_THROW == False:
            MOTOR_GROUP_THROW.spin(REVERSE, 100, PERCENT)
            MOTOR_GROUP_INTAKE.spin(REVERSE, 100, PERCENT)
            IS_THROW=True
        if IS_THROW and CONTROLLER.buttonA.pressing() == False:
            MOTOR_GROUP_THROW.stop()
            MOTOR_GROUP_INTAKE.stop()
            IS_THROW=False
        if CONTROLLER.buttonR1.pressing() and IS_TAKE_OUT == False:
            MOTOR_GROUP_INTAKE.spin(FORWARD, 100, PERCENT)
            IS_TAKE_OUT=True
        if IS_TAKE_OUT and CONTROLLER.buttonR1.pressing() == False:
            MOTOR_GROUP_INTAKE.stop()
            IS_TAKE_OUT=False
        if CONTROLLER.buttonR2.pressing() and IS_TAKE_IN == False:
            MOTOR_GROUP_INTAKE.spin(REVERSE, 100, PERCENT)
            IS_TAKE_IN=True
        if IS_TAKE_IN and CONTROLLER.buttonR2.pressing() == False:
            MOTOR_GROUP_INTAKE.stop()
            IS_TAKE_IN=False
        wait(20)

def onauton_autonomous_0():
    DRIVETRAIN.drive_for(FORWARD, 500, MM, 100, PERCENT)
    MOTOR_GROUP_INTAKE.__spin_for_time(REVERSE, 1000, MSEC, 100, PERCENT)
    DRIVETRAIN.drive_for(REVERSE, 550, MM, 100, PERCENT)

def printToScreen(func, err=0):
    if err == 0:
        CONTROLLER.screen.print("[ {} ] No errors throw: at <{}>".format(PETER_GRIFFN.timer.time(MSEC), func))
        CONTROLLER.screen.new_line()
    else:
        CONTROLLER.screen.print("[ {} ] Error {}: at <{}>".format(PETER_GRIFFN.timer.time(MSEC), err, func))
        CONTROLLER.screen.new_line()

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

def skills():
    printToScreen("skills",0)

# register the competition functions
START_TIME = PETER_GRIFFN.timer.time(MSEC)
while (START_TIME < 5000):
    if CONTROLLER.buttonA.pressing():
        skills()
competition = Competition( vexcode_driver_function, vexcode_auton_function )