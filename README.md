# Vision Based Cube Solver
## Overview 
This project implements a algorithm for a baxter robot to solve a disrupted cube. The process are stated below.

### 1. initizlize.py  
This file would initizlize the entire system and make sure the baxter robot is functonal and in it's default position. Then the Baxter robot would pick up the cube on it's command and take pictures of each sides of the cube and put the cube back with it's original position. In the process, the environment light is dark to for better recognition. (see side1.jpg in "for pdf" we can find it is hard to tell the difference between yellow and white.)  
### 2. color_rec.py  
This file will read the images that the robot just took and zoom in for the cube. Then it will enhance the image and recognize the color with HSV color representation and write it's result to a file. You can find differnet image with different method. 
### 3.solver.py      
This file will call a open source cube solving algorithm and solve the cube. Then the generated commands will be translated to some basic movements that I defined in the script. With these movemnets the baxter could solve the cube. After each movement, there is a recalibration process for the robot. Basicially, the recalibration process it to move the cube slightly every time it moves to make sure it is in the same spot when it has been picked up. 
### 4.Cube_simulator.py  
This file is a cube simulator, with color of each block of the cube imported, the script can simulate the cube and response to every move instruction to test the validity of the cube solver.  

### 5.Demo Video
https://drive.google.com/file/d/1N2JtJ2zYXBZTWNWIwz844KzQimZScZX1/view?usp=sharing

## Usage 
run "python initizlize.py", "python color_rec.py", "python solver.py".  

Make sure that you use Python 3 and a fully functioning baxter robot.

