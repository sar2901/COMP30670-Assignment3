

# LIGHT TESTER #
*** Program to count LED lights ***
-----------------------------------

## GitHub Repository ##
#### https://github.com/sar2901/COMP30670_Assignment3


## Purpose ##
The Science Centre is installing a new display board which is constructed from LED lights.
The board is a square grid of LEDs.

This program tests the lights by sending instructions to turn on, turn off, or switch various inclusive ranges given as coordinate pairs.
These instructions will be read from a file and the program will determine how many lights are on after al the instructions have been applied.


## Requirements ##
*pytest*

## Installation ##

pip install -e .

### TEST ###
Test can be executed by running the test.py file.
py.test tests/test.py

Code will test for various things: 
* Existence of the input file
* Check for errors in file, any commands which are not "turn on". "turn off" or "switch" should be ignored
* If a command affects a region outside the area of hte grid, then it will still be executed, but only on the region of lights inside the boundary


## RUN ##

In command line:
* LEDCounter --input {file} *

Files to run:
1. LEDCounter --input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt 
2. LEDCounter --input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt 
3. LEDCounter --input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt 
4. LEDCounter --input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt 
5. LEDCounter --input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt 
