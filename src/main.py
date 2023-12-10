from vex import *
import math

brain=Brain()
controller=Controller(PRIMARY)
motor_l=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_r=Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
motor_group_l=MotorGroup(motor_l)
motor_group_r=MotorGroup(motor_r)
drivetrain=DriveTrain(motor_group_l, motor_group_r)
motor_top=Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
motor_bottom=Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
motor_group_throw=MotorGroup(motor_top, motor_bottom)
motor_front_left=Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
motor_front_right=Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
motor_group_intake=MotorGroup(motor_front_left, motor_front_right)
hasObject=True
dead_zone=10
inMotion=False
isSkill=False
isThrow=False
isTakeOut=False
isTakeIn=False

def ondriver_drivercontrol_0():
    global hasObject, dead_zone, inMotion, isSkill, isThrow, isTakeOut, isTakeIn
    while competition.is_enabled and competition.is_driver_control:
        if controller.axis1.position() > dead_zone or controller.axis1.position() < -dead_zone:
            drivetrain.turn(RIGHT, controller.axis1.position()*0.5, PERCENT)
            inMotion=True
        if controller.axis3.position() > dead_zone or controller.axis3.position() < -dead_zone:
            drivetrain.drive(FORWARD, controller.axis3.position(), PERCENT)
            inMotion=True
        if controller.axis3.position() == 0 and controller.axis1.position() == 0 and inMotion:
            drivetrain.stop()
            inMotion=False
        if controller.buttonA.pressing() and isThrow == False:
            motor_group_throw.spin(REVERSE, 100, PERCENT)
            motor_group_intake.spin(REVERSE, 100, PERCENT)
            isThrow=True
        if isThrow and controller.buttonA.pressing() == False:
            motor_group_throw.stop()
            motor_group_intake.stop()
            isThrow=False
        if controller.buttonR1.pressing() and isTakeOut == False:
            motor_group_intake.spin(FORWARD, 100, PERCENT)
            isTakeOut=True
        if isTakeOut and controller.buttonR1.pressing() == False:
            motor_group_intake.stop()
            isTakeOut=False
        if controller.buttonR2.pressing() and isTakeIn == False:
            motor_group_intake.spin(REVERSE, 100, PERCENT)
            isTakeIn=True
        if isTakeIn and controller.buttonR2.pressing() == False:
            motor_group_intake.stop()
            isTakeIn=False
        wait(20)

def onauton_autonomous_0():
    drivetrain.drive_for(FORWARD, 500, MM, 100, PERCENT)
    motor_group_intake.__spin_for_time(REVERSE, 1000, MSEC, 100, PERCENT)
    drivetrain.drive_for(REVERSE, 550, MM, 100, PERCENT)

def printToBrain(func, err=0):
    if err == 0:
        brain.screen.print("[ {} ] No errors throw: at <{}>".format(brain.timer.time(MSEC), func))
        brain.screen.new_line()
    else:
        brain.screen.print("[ {} ] Error {}: at <{}>".format(brain.timer.time(MSEC), err, func))
        brain.screen.new_line()

def goto(x,y,vel,speed):
    current_position=None

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