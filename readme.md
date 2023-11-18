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
- A [BRAKE]
- B []
- Y []
- D-PAD Up [COAST]
- D-PAD Down [BRAKE]
- D-PAD Left []
- D-PAD Right []
- Axis 1 [LEFT/RIGHT]
- Axis 2 []
- Axis 3 [FORWARD/BACKWARD]
- Axis 4 []
- L1 [CHOOSE RED OFFENCE]
- L2 [CHOOSE Red DEFENCE]
- R1 [CHOOSE Blue DEFENCE]
- R2 [CHOOSE BLUE OFFENCE]

## Robot Details
Our robot, labeled 10930C, is equipped with the following components:

- **Chassis**: We've chosen the Speedbot chassis, which features rear-wheel drive with omni-wheels in the front and traction wheels in the back. This chassis is powered by two motors.

- **Catapult Launcher**: Our robot utilizes a catapult launching system that stores energy using a ratchet system. This stored energy can be released quickly to launch the tri-ball. The catapult launcher is powered by one motor.

- **Fly-Wheel Intake System**: The fly-wheel intake system employs a set of arms with spinning wheels. It is responsible for efficiently handling and collecting game elements. This system also uses one motor.

### Ports List

- Port1 [left_drive_motor]
- Port2 []
- Port3 []
- Port4 []
- Port5 []
- Port6 [radio]
- Port7 []
- Port8 []
- Port9 []
- Port10 [right_drive_motor]
- Port11 []
- Port12 []
- Port13 []
- Port14 []
- Port15 []
- Port16 []
- Port17 []
- Port18 []
- Port19 []
- Port20 []
- PortA []
- PortB []
- PortC []
- PortD []
- PortE []
- PortF []
- PortG []

## Application Details
In the `main.py` file, you will find the code that controls the robot's movements, runs autonomous routines, and manages other important functions for the VEX Over Under competition. Use `git clone https://github.com/vx-clutch/vrc-python-app.git` to clone the repository with git

#### How to Read the Console

- 0: No Errors
- -1: Unknown Error
- 1: Unexpected Value

## Autonomous Routine
The autonomous routine for our robot is field position-dependent. The following list shows the different strategies for the 15-second autonomous period.  

## Contributors

- [vx_clutch](https://github.com/vx-clutch)

## License
Copyright <2023> <vx-clutch>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
