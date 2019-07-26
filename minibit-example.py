#Import the library
from minibit import *

#Initalize the robot
robot = miniBit()

for i in range(4): #Loop 4 times (There are 4 LEDs)
    robot.leds[i] = (255, 0, 0) #Set them all to red
    robot.leds.show() #Show the changes

robot.forward(600) #Make the robot go forward at speed 600
sleep(1000) #Sleep for 1 second
robot.left(600) #Make the robot go left at speed 600
sleep(1000) #Sleep for 1 second
robot.right(600) #Make the robot go right at speed 600
sleep(1000) #Sleep for 1 second
robot.stop() #Make the stop with the brake

robot.backward(600) #Make the robot reverse at speed 600
sleep(1000) #Sleep for 1 second
robot.stop(brake=False) #Make the stop without the brake

while True: #Create a "forever" loop
    display.scroll(robot.sonar_cm()) #Scroll the distance read by the sonar sensor in cm
    sleep(500) #Sleep for half a second
    display.scroll(robot.sonar_mm()) #Scroll the distance read by the sonar sensor in mm






