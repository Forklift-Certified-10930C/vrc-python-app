from vex import *
brain=Brain()
controller=Controller()
motorL=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motorR=Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
motorGroupL=MotorGroup(motorL)
motorGroupR=MotorGroup(motorR)
drivetrain=DriveTrain(motorGroupL, motorGroupR)
motorTop=Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
motorBottom=Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
motorGroupThrow=MotorGroup(motorTop, motorBottom)
selectedPosition=None
hasObject=True
deadZone=10
inMotion=False
isSkill=False
throwToggle=False
def printToBrain(err, func):
    if err == 0:
        brain.screen.print("[ {} ] No errors throw: at <{}>".format(brain.timer.time(TimeUnits.MSEC), err, func))
    else:
        brain.screen.print("[ {} ] Error {}: at <{}>".format(brain.timer.time(TimeUnits.MSEC), err, func))
        brain.screen.new_line()
def throwObject():
    motorGroupThrow.__spin_for_time(FORWARD, 1, SECONDS, 100, PERCENT)
    return 0, 'throwObject'
def pickObject():
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
        drivetrain.turn_for(RIGHT, 90/2, DEGREES)
        result, functionName=pickObject()
        printToBrain(result, functionName)
        printToBrain(0,'autonomous')
    if selectedPosition == 'Red Defence' or selectedPosition == 'Blue Defence':
        drivetrain.drive_for(FORWARD, 1800, MM)
        drivetrain.turn_for(RIGHT, 90/2, DEGREES)
        result, functionName=throwObject()
        printToBrain(result, functionName)
        printToBrain(0,'autonomous')
def driverControl():
    global selectedPosition, hasObject, deadZone, inMotion, isSkill, throwToggle
    while competition.is_enabled() and competition.is_driver_control():
        if controller.axis1.position() > deadZone or controller.axis1.position() < -deadZone:
            drivetrain.drive(RIGHT, controller.axis1.position(), PERCENT)
            inMotion=True
        if controller.axis3.position() > deadZone or controller.axis3.position() < -deadZone:
            drivetrain.drive(FORWARD, controller.axis3.position(), PERCENT)
            inMotion=True
        if controller.buttonA.pressing():
            result, functionName=throwObject()
            printToBrain(result, functionName)
        if controller.buttonB.pressing():
            if throwToggle:
                throwToggle=False
                motorGroupThrow.stop()
            else:
                motorGroupThrow.spin(FORWARD, 100, PERCENT)
        wait(20)
result, functionName, position=teamChoosing()
selectedPosition=position
printToBrain(result, functionName)
competition=Competition(driverControl, autonomous)