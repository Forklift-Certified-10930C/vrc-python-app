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
def printToBrain(err, func):
    error_message = "[ {} ] Error {}:\n at {}".format(brain.timer.time(TimeUnits.MSEC), err, func)
    brain.screen.print(error_message)
    brain.screen.new_line()
def handleObject():
    if hasObject:
        return 0, 'handleObject'
    else:
        return 0, 'handleObject'
def throwObject():
    if hasObject:
        return 1
    else:
        return 0, 'throwObject'
def teamChoosing():
    while selectedPosition is None:
        if controller.buttonL1.pressing():
            brain.screen.draw_image_from_file("red_offence.png", 0, 0)
            return 0, 'teamChoosing', "red_offence"
        if controller.buttonL2.pressing():
            brain.screen.draw_image_from_file("red_defence.png", 0, 0)
            return 0, 'teamChoosing', "red_defence"
        if controller.buttonR1.pressing():
            brain.screen.draw_image_from_file("blue_offence.png", 0, 0)
            return 0, 'teamChoosing', "blue_offence"
        if controller.buttonR2.pressing():
            brain.screen.draw_image_from_file("blue_defence.png", 0, 0)
            return 0, 'teamChoosing', "blue_defence"
        wait(20)
    wait(1000)
    brain.screen.clear_screen()
def autonomous():
    global selectedPosition
    drivetrain.set_stopping(BRAKE)
    if selectedPosition == 'Red Offence' or selectedPosition == 'Blue Offence':
        drivetrain.drive_for(FORWARD, 1800, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 500, MM)
        result, functionName=handleObject()
        printToBrain(result, functionName)
        return 0, 'autonomous'
    if selectedPosition == 'Red Defence' or selectedPosition == 'Blue Defence':
        drivetrain.drive_for(FORWARD, 1000, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        result, functionName=throwObject()
        printToBrain(result, functionName)
        return 0, 'autonomous'
def driverControl():
    global selectedPosition, hasObject, deadZone, inMotion
    while True:
        if inMotion != 0:
            inMotion = True
        if controller.buttonUp.pressing():
            drivetrain.set_stopping(COAST)
        if controller.buttonDown.pressing():
            drivetrain.set_stopping(BRAKE)
        if controller.buttonA.pressing():
            drivetrain.stop()
            inMotion = False
        if controller.axis3.position != 0:
            drivetrain.drive(FORWARD, controller.axis3.position(), PERCENT)
        if controller.axis1.position != 0:
            drivetrain.turn(FORWARD, controller.axis1.position(), PERCENT)
result, functionName, selectedPosition=teamChoosing()
competition = Competition(driverControl(), autonomous())