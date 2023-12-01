from vex import *

myVariable = 0
brain=Brain()

def when_started1():
    global myVariable
    pass

def ondriver_drivercontrol_0():
    global myVariable
    printToBrain(0, "driver")
    pass

def onauton_autonomous_0():
    global myVariable
    printToBrain(0, "auton")
    pass

def printToBrain(err, func):
    if err == 0:
        brain.screen.print("[ {} ] No errors throw: at <{}>".format(brain.timer.time(MSEC), err, func))
    else:
        brain.screen.print("[ {} ] Error {}: at <{}>".format(brain.timer.time(MSEC), err, func))
        brain.screen.new_line()

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

when_started1()
