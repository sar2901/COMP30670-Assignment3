#COMP30670_Assignment3/LEDCounter

'''
Created on Mar 1, 2018
@author: Sybilla Robertson
'''
import urllib.request
import re
import argparse
import requests

def readInput(file):
    #Function that opens input file
    
    if file.startswith('http'):
        req = requests.get(file)
        return req.iter_lines(decode_unicode=True)
    else:
        openFile = open(file)
        return openFile

class lightGrid():
    #Class to handle light functionality
    def __init__(self, size):
        self.gridSize = size
        self.light = self.createLEDArray()

    def createLEDArray(self):
        #Fuction to create starting LED array
        return [[False for _ in range(self.gridSize)] for _ in range(self.gridSize)]

    def checkCoords(self, coordRange):
        #Function that checks if coordinates are out of range
        return tuple(min(max(0, i), self.gridSize - 1) for i in coordRange)

    def changeLight(self, start, end, instruction):
        #Function to change light according to instruction parameters
        start = self.checkCoords(start)
        end = self.checkCoords(end)
        for j in range(start[1], end[1] + 1):
            for i in range(start[0], end[0] + 1):
                self.light[i][j] = instruction(self.light[i][j])

    def countLights(self):
        #Function to sum number of lights on
        lightsOn = 0
        for line in self.light:
            lightsOn += sum(line)
        return lightsOn


def parseFile(line):
    #Function to parse lines in input file using RegEx to find coordinates. Applies functions according to string values
    pair = re.findall("(-*\d+).*?(-*\d+)", line)
    line = line.split()
    start, end = pair
    start = int(start[0]), int(start[1])
    end = int(end[0]), int(end[1])


    if line[0] == 'switch':
        action = switch
    elif line[0] == 'turn' and line[1] == 'on':
        action = on
    elif line[0] == 'turn' and line[1] == 'off':
        action = off
    else:
        return None
    return start, end, action


def on(light):
    #Function to turn light on
    return True


def off(light):
    #Function to turn light off
    return False


def switch(light):
    #Function to switch light state
    return not light


def main():
   #Main function to read console input

    parser = argparse.ArgumentParser(prog='light_box')
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    url = args.input

    if not url:
        print("Please use -h for help.")
        return 1

    lightGridStatus(url)


def lightGridStatus(url):
    # Function to read parsed arguments
    
    buffer = readInput(url)
    grid = lightGrid(size=int(next(buffer)))

    for line in buffer:
        if line:
            result = parseFile(line)
            if result:
                start, end, action = result
                grid.changeLight(start, end, action)

    #Print number of lights on
    print("Number of lights on:", grid.countLights())


if __name__ == '__main__':
    main()
