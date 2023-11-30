from vex import *
brainInit=Brain()
controllerInit=Controller()
motor1=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor10=Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
motor5=Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
motor8=Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
motorU=None
motorUn=None
throwMotorsInit=MotorGroup(motor5,motor8)
intakeMotorsInit=MotorGroup(motorU,motorUn)
driveTrainInit=DriveTrain(motor1, motor10)

selectedPosition=None
deadZone=10
inMotion=False
isSkill=False
throwToggle=False

def printToBrain(func,err=0):
    if err == 0:
        brainInit.screen.print("[ {} ] No errors thrown: at <{}>".format(brainInit.timer.time(TimeUnits.MSEC), err, func))
    else:
        brainInit.screen.print("[ {} ] Error {}: at <{}>".format(brainInit.timer.time(TimeUnits.MSEC), err, func))
        brainInit.screen.new_line()

class Robot:
    def __init__(self, drivetrain, throwmotors, controller, brain, intakemotors):
        self.drivetrain=drivetrain
        self.throwmotors=throwmotors
        self.controller=controller
        self.brain=brain
        self.intakemotors=intakemotors
    def forward(self):
        drivetrain=self.drivetrain
        controller=self.controller
        drivetrain.drive(FORWARD, controller.axis3.position(), PERCENT)
    def turn(self):
        drivetrain=self.drivetrain
        controller=self.controller
        drivetrain.turn(RIGHT, controller.axis1.position(), PERCENT)
    def stop(self):
        drivetrain=self.drivetrain
        drivetrain.stop()
    def throw(self):
        controller=self.controller
        throwmotors=self.throwmotors
        throwmotors.__spin_for_time(FORWARD, 1, SECONDS, 100, PERCENT)
    def drivefor(self, dist):
        drivetrain=self.drivetrain
        controller=self.controller
        drivetrain.drive_for(FORWARD, dist, MM)
    def turnfor(self, deg):
        drivetrain=self.drivetrain
        controller=self.controller
        drivetrain.turn_for(RIGHT, deg, DEGREES)
    def pickObject(self):
        pass

robot=Robot(driveTrainInit, throwMotorsInit, controllerInit, brainInit, intakeMotorsInit)

def teamChoosing():
    global isSkill
    while True:
        if controllerInit.buttonL1.pressing():
            brainInit.screen.draw_image_from_file("red_offence.png", 0, 0)
            while controllerInit.buttonL1.pressing():
                wait(5, MSEC)
            brainInit.screen.clear_screen()
            return 'teamChoosing', "Red Offence"
        if controllerInit.buttonL2.pressing():
            brainInit.screen.draw_image_from_file("red_defence.png", 0, 0)
            while controllerInit.buttonL2.pressing():
                wait(5, MSEC)
            brainInit.screen.clear_screen()
            return 'teamChoosing', "Red Defence"
        if controllerInit.buttonR1.pressing():
            brainInit.screen.draw_image_from_file("blue_offence.png", 0, 0)
            while controllerInit.buttonR1.pressing():
                wait(5, MSEC)
            brainInit.screen.clear_screen()
            return 'teamChoosing', "Blue Offence"
        if controllerInit.buttonR2.pressing():
            brainInit.screen.draw_image_from_file("blue_defence.png", 0, 0)
            while controllerInit.buttonR2.pressing():
                wait(5, MSEC)
            brainInit.screen.clear_screen()
            return 'teamChoosing', "Blue Defence"
        if controllerInit.buttonA.pressing():
            brainInit.screen.draw_image_from_file("blue_defence.png", 0, 0)
            while controllerInit.buttonA.pressing():
                wait(5, MSEC)
            brainInit.screen.clear_screen()
            isSkill=True
            return 'teamChoosing', "Skill"
        wait(20)

def autonomous():
    global selectedPosition
    driveTrainInit.set_stopping(BRAKE)
    if selectedPosition == 'Red Offence' or selectedPosition == 'Blue Offence':
        robot.drivefor(FORWARD, 1800, MM)
        robot.turnfor(RIGHT, 90/2, DEGREES)
        printToBrain('autonomous')
    if selectedPosition == 'Red Defence' or selectedPosition == 'Blue Defence':
        robot.drivefor(FORWARD, 1800, MM)
        robot.turnfor(LEFT, 90/2, DEGREES)
        robot.throw()
        printToBrain('autonomous')
    if selectedPosition == 'skill':
        printToBrain('autonomous')

def drivercontrol():
    global deadZone, inMotion, throwToggle

selectedPosition=teamChoosing()
comp=Competion(drivercontrol, autonomous)