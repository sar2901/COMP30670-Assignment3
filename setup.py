#COMP30670_Assignment3/

'''
Created on Feb 27, 2018
@author: Sybilla Robertson
'''
from setuptools import setup

setup(name="LEDCounter",
      version="0.1.0",
      description="COMP30670 Assingment3 LED Counter",
      url="",
      author="Sybilla Robertson",
      author_email="sybilla.robertson@ucdconnect.ie",
      license="GPL3",
      packages=['LEDCounter'],
      test_suite="tests",
      entry_points={
          'console_scripts':['LEDCounter=LEDCounter.main:main']
          }
      )
