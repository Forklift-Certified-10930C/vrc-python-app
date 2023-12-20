from vex import *

BRIAN=Brain()
CONTROLLER=Controller(PRIMARY)
MOTOR_1=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
MOTOR_2=Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
MOTOR_GROUP_L=MotorGroup(MOTOR_1)
MOTOR_GROUP_R=MotorGroup(MOTOR_2)
DRIVETRAIN=DriveTrain(MOTOR_GROUP_L, MOTOR_GROUP_R)
MOTOR_7=Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
MOTOR_5=Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
MOTOR_GROUP_THROW=MotorGroup(MOTOR_7, MOTOR_5)
MOTOR_3=Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
MOTOR_8=Motor(Ports.PORT8, GearSetting.RATIO_6_1, True)
MOTOR_GROUP_INTAKE=MotorGroup(MOTOR_3, MOTOR_8)
MOTOR_4=Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
MOTOR_9=Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
MOTOR_GROUP_ARMS=MotorGroup(MOTOR_4, MOTOR_9)
HAS_OBJ=True
DEAD_ZONE=10
IN_MOTION=False
isSkill=False
IS_THROW=False
IS_TAKE_OUT=False
IS_TAKE_IN=False
IS_SKILLS=False
WING_STATUS=False
START_ANGLE_4=0
START_ANGLE_9=0

def ondriver_drivercontrol_0():
    global HAS_OBJ, DEAD_ZONE, IN_MOTION, isSkill, IS_THROW, IS_TAKE_OUT, IS_TAKE_IN, WING_STATUS
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
        if WING_STATUS == False and CONTROLLER.buttonX.pressing():
            arms(True)
            WING_STATUS=True
        if WING_STATUS and CONTROLLER.buttonX.pressing():
            arms(False)
            WING_STATUS=False
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
        BRIAN.screen.print("[ {} ] No errors throw: at <{}>".format(BRIAN.timer.time(MSEC), func))
        BRIAN.screen.new_line()
    else:
        BRIAN.screen.print("[ {} ] Error {}: at <{}>".format(BRIAN.timer.time(MSEC), err, func))
        BRIAN.screen.new_line()

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

def arms(pos):
    global START_ANGLE_4, START_ANGLE_9
    if pos:
        MOTOR_GROUP_ARMS.spin_to_position(90, DEGREES, 100 ,PERCENT)
    else:
        MOTOR_4.spin_to_position(START_ANGLE_4, DEGREES, 25, PERCENT)
        MOTOR_9.spin_to_position(START_ANGLE_9, DEGREES, 25, PERCENT)

def calibrate():
    global START_ANGLE_4, START_ANGLE_9
    START_ANGLE_4=MOTOR_4.position(DEGREES)
    START_ANGLE_9=MOTOR_9.position(DEGREES)
calibrate()

def skills():
    printToScreen("skills")
    MOTOR_GROUP_THROW.spin(REVERSE, 60, PERCENT)
    MOTOR_GROUP_INTAKE.spin(REVERSE, 60, PERCENT)
    wait(60000,MSEC)
    MOTOR_GROUP_THROW.stop()
    MOTOR_GROUP_INTAKE.stop()

BRIAN.screen.print('Proceed to skills? [ Y / N ]')
BRIAN.screen.new_line()
while True:
    if CONTROLLER.buttonA.pressing():
        IS_SKILLS=True
        BRIAN.screen.clear_line()
        CONTROLLER.rumble("..--")
        skills()
        break
    if CONTROLLER.buttonB.pressing():
        CONTROLLER.rumble(".")
        competition = Competition( vexcode_driver_function, vexcode_auton_function )
        BRIAN.screen.clear_line()
        break