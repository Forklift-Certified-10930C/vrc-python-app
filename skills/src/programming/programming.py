from vex import *

brain=Brain()
controller=Controller(PRIMARY)
gps=Gps(Ports.PORT22)
inertial=Inertial(Ports.PORT22)
color=Optical(Ports.PORT22)
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

def printToScreen(func, err):
    if err == 0:
        controller.screen.print("[ {} ] No errors throw: at <{}>".format(brain.timer.time(MSEC), func))
        controller.screen.new_line()
    else:
        controller.screen.print("[ {} ] Error {}: at <{}>".format(brain.timer.time(MSEC), err, func))
        controller.screen.new_line()

def goto(x,y,speed,wait):
    b=x-gps.x_position(MM)
    hypotenuse=y-gps.y_position(MM)
    if abs(b) < 1 and abs(hypotenuse) < 1:
        pass
    else:
        a=math.sqrt(b**2+hypotenuse**2)
        angle=math.asin(((math.sin(90/180.0*math.pi)*b)/a)/math.pi*180)
        if hypotenuse<0:
            angle=180-angle
            drivetrain.turn_to_heading(angle, DEGREES)
            drivetrain.drive_for(FORWARD, 1, MM, speed, PERCENT, wait=wait)

def main():
    pass

def vexcode_coding_skills():
    skill_task_0 = Thread( main )
    while(competition.is_autonomous() and competition.is_enabled() ):
        wait(10,MSEC)
    skill_task_0.stop()

def vexcode_placeholder_function():
    pass

# register the competition functions
competition = Competition( vexcode_placeholder_function, vexcode_coding_skills )