## VRC Python App

# 10930C

## Table Of Contents
 - [Introduction](#Introduction)
 - [Controls](#Controls)
 - [Robot Details](#Robot-Details)
 - [Application Details](#Application-Details)
 - [License](#License)

## Introduction
Welcome to our VRC Python Project! This document serves as a comprehensive guide to understanding our project. We've created this file with the aim of explaining how to control the robot as well as how to navigate this project.

## Controls
Here's a brief overview of the controls for our robot:

- X []
- A []
- B []
- Y []
- D-PAD Up []
- D-PAD Down []
- D-PAD Left []
- D-PAD Right []
- Axis 1 []
- Axis 2 [LEFT/RIGHT]
- Axis 3 [FORWARD/BACKWARD]
- Axis 4 []
- RB []
- LB []
- RT []
- LT []

## Robot Details
Our robot, labeled 10930C, is equipped with the following components:

- **Chassis**: We've chosen the Speedbot chassis, which features rear-wheel drive with omni-wheels in the front and traction wheels in the back. This chassis is powered by two motors.

- **Catapult Launcher**: Our robot utilizes a catapult launching system that stores energy using a ratchet system. This stored energy can be released quickly to launch the tri-ball. The catapult launcher is powered by one motor.

- **Fly-Wheel Intake System**: The fly-wheel intake system employs a set of arms with spinning wheels. It is responsible for efficiently handling and collecting game elements. This system also uses one motor.

## Application Details
In the `main.py` file, you will find the code that controls the robot's movements, runs autonomous routines, and manages other important functions for the VEX Over Under competition. Us `git clone https://github.com/vx-clutch/vrc-python-app.git` to clone the repository with git

## Autonomous Routine
The autonomous routine for our robot is field position dependant. The following list shows the differnt stratagys for the 15 second autonomous period.  

### Blue Alliance

- **Blue Side**: Lauch pre-loaded game element into red net

- **Red Side**:

### Red Alliance

- **Blue Side**:

- **Red Side**: Lauch pre-loaded game element into blue net

## License
Copyright <2023> <vx-clutch>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.