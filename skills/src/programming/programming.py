from vex import *

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