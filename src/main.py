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
        brain.screen.print("[ {} ] No errors thrown: at <{}>".format(brain.timer.time(TimeUnits.MSEC), err, func))
    else:
        brain.screen.print("[ {} ] Error {}: at <{}>".format(brain.timer.time(TimeUnits.MSEC), err, func))
        brain.screen.new_line()

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

robot=Robot(driveTrainInit, throwMotorsInit, controllerInit, brainInit, intakeMotorsInit)

def teamChoosing():
    global isSkill
    while True:
        if controller.buttonL1.pressing():
            brain.screen.draw_image_from_file("red_offence.png", 0, 0)
            while controller.buttonL1.pressing():
                wait(5, MSEC)
            brain.screen.clear_screen()
            return 0, 'teamChoosing', "Red Offence"
        if controller.buttonL2.pressing():
            brain.screen.draw_image_from_file("red_defence.png", 0, 0)
            while controller.buttonL2.pressing():
                wait(5, MSEC)
            brain.screen.clear_screen()
            return 0, 'teamChoosing', "Red Defence"
        if controller.buttonR1.pressing():
            brain.screen.draw_image_from_file("blue_offence.png", 0, 0)
            while controller.buttonR1.pressing():
                wait(5, MSEC)
            brain.screen.clear_screen()
            return 0, 'teamChoosing', "Blue Offence"
        if controller.buttonR2.pressing():
            brain.screen.draw_image_from_file("blue_defence.png", 0, 0)
            while controller.buttonR2.pressing():
                wait(5, MSEC)
            brain.screen.clear_screen()
            return 0, 'teamChoosing', "Blue Defence"
        if controller.buttonA.pressing():
            brain.screen.draw_image_from_file("blue_defence.png", 0, 0)
            while controller.buttonA.pressing():
                wait(5, MSEC)
            brain.screen.clear_screen()
            isSkill=True
            return 0, 'teamChoosing', "Skill"
        wait(20)

def autonomous():
    global selectedPosition
    drivetrain.set_stopping(BRAKE)
    if selectedPosition == 'Red Offence' or selectedPosition == 'Blue Offence':
        robot.drivefor(FORWARD, 1800, MM)
        robot.turnfor(RIGHT, 90/2, DEGREES)
        result, functionName=pickObject()
        printToBrain(result, functionName)
        printToBrain(0,'autonomous')
    if selectedPosition == 'Red Defence' or selectedPosition == 'Blue Defence':
        robot.drivefor(FORWARD, 1800, MM)
        robot.turnfor(LEFT, 90/2, DEGREES)
        result, functionName=throwObject()
        printToBrain(result, functionName)
        printToBrain(0,'autonomous')
    if selectedPosition == 'skill':
        printToBrain(0,'autonomous')

def drivercontrol():
    global deadZone, inMotion, throwToggle
    