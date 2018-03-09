#COMP30670_Assignment3/tests/
'''
Created on Feb 28, 2018
@author: Sybilla Robertson
'''
import sys
sys.path.append('.')
import unittest
from LEDCounter.main import main, readInput, lightGrid, parseFile, on, off, switch, lightGridStatus


class LEDCounterTest(unittest.TestCase):

    def setUp(self):
        self.inputTest = "testinput.txt"

    def readInputTest(self):
        readInput(self.inputTest)

    def parseSwitchTest(self):
        start, end, fun = parseFile('switch 0,0 through 4,4')
        self.assertEquals(start, (322 , 558))
        self.assertEquals(end, (977 , 958))

    def parseOnOffTest(self):
        start, end, fun = parseFile('turn on 0,0 through 4,4')
        self.assertEquals(start, (0,0))
        self.assertEquals(end, (4,4))

        start, end, fun = parseFile('turn off 0,0 through 4,4')
        self.assertEquals(start, (0,0))
        self.assertEquals(end, (4,4))

    def onOffSwitchTest(self):
        self.assertTrue(on(True))
        self.assertTrue(on(False))
        self.assertFalse(off(True))
        self.assertFalse(off(False))
        self.assertFalse(switch(True))
        self.assertTrue(switch(False))

    def mainTest(self):
        lightGridStatus(self.test_file)

if __name__ == '__main__':
    unittest.main()
