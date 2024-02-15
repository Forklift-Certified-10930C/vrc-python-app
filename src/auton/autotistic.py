from vex import *
 
BRIAN=Brain()
CONTROLLER=Controller(PRIMARY)

MOTOR_7=Motor(Ports.PORT7, GearSetting.RATIO_36_1, True)
MOTOR_9=Motor(Ports.PORT9, GearSetting.RATIO_6_1, False)  
MOTOR_10=Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
MOTOR_11=Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
MOTOR_17=Motor(Ports.PORT17, GearSetting.RATIO_36_1, False)
MOTOR_19=Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)
MOTOR_20=Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)

MOTOR_GROUP_L=MotorGroup(MOTOR_20)
MOTOR_GROUP_R=MotorGroup(MOTOR_10)
MOTOR_GROUP_LAUNCHER=MotorGroup(MOTOR_7,MOTOR_17)
MOTOR_GROUP_INTAKE=MotorGroup(MOTOR_9, MOTOR_19)
MOTOR_GROUP_WINGS=MotorGroup(MOTOR_11)

DRIVETRAIN=DriveTrain(MOTOR_GROUP_L, MOTOR_GROUP_R)

# Settings
DEAD_ZONE_PERCENT=10
LAUNCHER_VEL_PERCENT=30
INTAKE_SPEED_PERCENT=100
TURN_DAMP_PERCENT=0.5
LAUNCHER_SPEED_PERCENT=25
LAUNCHER_DEFAULT_POSITION_DEGREES=135

AUTONOMOUS_SPEED_PERCENT=100
AUTONOMOUS_INTAKE_SPEED_PERCENT=100
AUTONOMOUS_INTAKE_TIME_MSEC=1000
AUTONOMOUS_DRIVE_DISTANCE_MM=500
AUTONOMOUS_DRIVE_DISTANCE_MM_MARGIN=50
AUTONOMOUS_ENABLED_BOOL=False

IN_MOTION=False
IS_SKILL=False
IS_LAUNCHER=False
IS_TAKE_OUT=False
IS_TAKE_IN=False
WING_STATUS=False
START_ANGLE_7=0
START_ANGLE_11=0

def ondriver_drivercontrol():
    global DEAD_ZONE_PERCENT, IN_MOTION, IS_SKILL, IS_LAUNCHER, IS_TAKE_OUT, IS_TAKE_IN, WING_STATUS
    while competition.is_enabled and competition.is_driver_control:
        if CONTROLLER.axis1.position() > DEAD_ZONE_PERCENT or CONTROLLER.axis1.position() < -DEAD_ZONE_PERCENT:
            DRIVETRAIN.turn(RIGHT, CONTROLLER.axis1.position()*TURN_DAMP_PERCENT, PERCENT)
            IN_MOTION=True
    
        if CONTROLLER.axis3.position() > DEAD_ZONE_PERCENT or CONTROLLER.axis3.position() < -DEAD_ZONE_PERCENT:
            DRIVETRAIN.drive(FORWARD, CONTROLLER.axis3.position(), PERCENT)
            IN_MOTION=True
        if CONTROLLER.axis3.position() == 0 and CONTROLLER.axis1.position() == 0 and IN_MOTION:
            DRIVETRAIN.stop()
            IN_MOTION=False

        if CONTROLLER.buttonA.pressing() and IS_LAUNCHER == False:
            MOTOR_GROUP_LAUNCHER.spin(FORWARD, LAUNCHER_VEL_PERCENT, PERCENT)
            IS_LAUNCHER=True
        if IS_LAUNCHER and CONTROLLER.buttonA.pressing() == False:
            MOTOR_GROUP_LAUNCHER.stop(COAST)
            IS_LAUNCHER=False
        
        #if WING_STATUS == False and CONTROLLER.buttonX.pressing():
            #wings(True)
            #WING_STATUS=True
            #while CONTROLLER.buttonX.pressing():
                #wait(10, MSEC)
        #if WING_STATUS and CONTROLLER.buttonX.pressing():
            #wings(False)
            #WING_STATUS=False
        
        if CONTROLLER.buttonR1.pressing() and IS_TAKE_OUT == False:
            MOTOR_GROUP_INTAKE.spin(REVERSE, INTAKE_SPEED_PERCENT, PERCENT)
            IS_TAKE_OUT=True
        if IS_TAKE_OUT and CONTROLLER.buttonR1.pressing() == False:
            MOTOR_GROUP_INTAKE.stop()
            MOTOR_GROUP_LAUNCHER.set_position(LAUNCHER_DEFAULT_POSITION_DEGREES, DEGREES)
            IS_TAKE_OUT=False

        if CONTROLLER.buttonR2.pressing() and IS_TAKE_IN == False:
            MOTOR_GROUP_INTAKE.spin(FORWARD, INTAKE_SPEED_PERCENT, PERCENT)
            IS_TAKE_IN=True
        if IS_TAKE_IN and CONTROLLER.buttonR2.pressing() == False:
            MOTOR_GROUP_INTAKE.stop()
            IS_TAKE_IN=False

        # if CONTROLLER.buttonUp.pressing():
            # MOTOR_GROUP_LAUNCHER.set_position(LAUNCHER_DEFAULT_POSITION_DEGREES, DEGREES)
        wait(20)
def onauton_autonomous():
    if AUTONOMOUS_ENABLED_BOOL:
        DRIVETRAIN.drive_for(FORWARD, AUTONOMOUS_DRIVE_DISTANCE_MM, MM, AUTONOMOUS_SPEED_PERCENT, PERCENT)
        MOTOR_GROUP_INTAKE.__spin_for_time(FORWARD, AUTONOMOUS_INTAKE_TIME_MSEC, MSEC, AUTONOMOUS_INTAKE_SPEED_PERCENT, PERCENT)
        DRIVETRAIN.drive_for(REVERSE, (AUTONOMOUS_DRIVE_DISTANCE_MM + AUTONOMOUS_DRIVE_DISTANCE_MM_MARGIN), MM, AUTONOMOUS_SPEED_PERCENT, PERCENT)
    else:
        MOTOR_GROUP_LAUNCHER.spin(FORWARD, LAUNCHER_SPEED_PERCENT, PERCENT)

def printErrToScreen(err, func):
    if err == 0:
        BRIAN.screen.print("[ {} ] No errors throw: at <{}>".format(BRIAN.timer.time(MSEC), func))
        BRIAN.screen.new_line()
    else:
        BRIAN.screen.print("[ {} ] Error {}: at <{}>".format(BRIAN.timer.time(MSEC), err, func))
        BRIAN.screen.new_line()

def printMsgToScreen(msg, func):
    BRIAN.screen.print("[ {} ] {} said {}".format(BRIAN.timer.time(MSEC), func, msg))
    BRIAN.screen.new_line()

def vexcode_auton_function():
    auton_task = Thread( onauton_autonomous)
    while( competition.is_autonomous() and competition.is_enabled() ):
        wait( 10, MSEC )
    auton_task.stop()

def vexcode_driver_function():
    driver_control_task = Thread( ondriver_drivercontrol )

    while( competition.is_driver_control() and competition.is_enabled() ):
        wait( 10, MSEC )
    driver_control_task.stop()

def wings(pos):
    global START_ANGLE_7, START_ANGLE_11
    if pos:
        MOTOR_11.spin_to_position(85, DEGREES, LAUNCHER_SPEED_PERCENT, PERCENT)
        MOTOR_7.spin_to_position(40, DEGREES, LAUNCHER_SPEED_PERCENT, PERCENT)
    else:
        MOTOR_11.spin_to_position(START_ANGLE_7, DEGREES, LAUNCHER_SPEED_PERCENT, PERCENT)
        MOTOR_7.spin_to_position(START_ANGLE_11, DEGREES, LAUNCHER_SPEED_PERCENT, PERCENT)

def calibrate():
    global START_ANGLE_7, START_ANGLE_11
    START_ANGLE_7=MOTOR_7.position(DEGREES)
    START_ANGLE_11=MOTOR_11.position(DEGREES)
calibrate()

competition = Competition( vexcode_driver_function, vexcode_auton_function )

