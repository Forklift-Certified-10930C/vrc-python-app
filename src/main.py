from vex import *
brain=Brain()
controller=Controller()
motorL=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motorR=Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
motorGroupL=MotorGroup(motorL)
motorGroupR=MotorGroup(motorR)
drivetrain=DriveTrain(motorGroupL, motorGroupR)
selectedPosition=None
hasObject=True
deadZone=10
inMotion=False
isSkill=False
def printToBrain(err, func):
    brain.screen.print("[ {} ] Error {}: at <{}>".format(brain.timer.time(TimeUnits.MSEC), err, func))
    brain.screen.new_line()
def throwObject():
    return 0, 'throwObject'
def handleObjectDown():
    return 0, 'handleObjectDown'
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
            brain.screen.draw_image_from_file("skill_confirmed.png", 0, 0)
            while controller.buttonA.pressing():
                wait(5, MSEC)
            isSkill=True
            brain.screen.clear_screen()
        wait(20)
def autonomous():
    global selectedPosition
    drivetrain.set_stopping(BRAKE)
    if selectedPosition == 'Red Offence' or selectedPosition == 'Blue Offence':
        drivetrain.drive_for(FORWARD, 1800, MM)
        drivetrain.turn_for(LEFT, 90/2, DEGREES)
        drivetrain.drive_for(FORWARD, 500, MM)
        result, functionName=handleObjectDown()
        printToBrain(result, functionName)
        return 0, 'autonomous'
    if selectedPosition == 'Red Defence' or selectedPosition == 'Blue Defence':
        drivetrain.drive_for(FORWARD, 1000, MM)
        drivetrain.turn_for(RIGHT, 90/2, DEGREES)
        result, functionName=throwObject()
        printToBrain(result, functionName)
        return 0, 'autonomous'
def driverControl():
    global selectedPosition, hasObject, deadZone, inMotion, isSkill
    while True:
        if controller.buttonUp.pressing():
            drivetrain.set_stopping(COAST)
        if controller.buttonDown.pressing():
            drivetrain.set_stopping(BRAKE)
        if abs(controller.axis3.position()) > deadZone:
            motorGroupL.spin(FORWARD, controller.axis3.position(), PERCENT)
            motorGroupR.spin(FORWARD, controller.axis3.position(), PERCENT)
            inMotion=True
        if abs(controller.axis1.position()) > deadZone:
            motorGroupL.spin(FORWARD, controller.axis1.position(), PERCENT)
            motorGroupR.spin(FORWARD, -1*(controller.axis1.position()), PERCENT)
            inMotion=True
        if controller.buttonB.pressing():
            result, functionName=throwObject()
            printToBrain(result, functionName)
            wait(20)
        if controller.axis1.position() < deadZone and controller.axis3.position() < deadZone and inMotion:
            motorGroupL.stop()
            motorGroupR.stop()
            inMotion=False
        wait(20)
result, functionName, position=teamChoosing()
selectedPosition=position
printToBrain(result, functionName)
autonomous()
driverControl()