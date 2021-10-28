#Alberto Benavides
#10-25-2021
#print Hello World
print ("Hello World")

#Alberto Benavides
#10-25-2021
#Takes the user input and put hello for a name
n = input ("Please enter your name ")
print ("Hello", n)

#Alberto Benavides
#10-25-2021
#A user input with 2 names and add if and or

n = input ("Please enter your name ")
#print ("Hello", n)
if n =="Alberto" or n =="Sunhwa":
    print ("hello", n)

#Alberto Benavides
#10-25-2021
# Accepts user input as the radius, and calculates the area of a circle using it.

p = float(input("enter the radius"))
import math
area = math.pi * p ** 2
print("The area of the circle is", area)

#Alberto Benavides
#10-25-2021
#Use the input for miles and gallons and caculate it.

m = int(input("What is the miles"))
g = int(input("What is the gallons"))
MPG = m/g
print(MPG)
print("The total of the car is",MPG)

#Alberto Benavides
#10-25-2021
#Convert degrees Fahrenhiet to degree celisus

DF = int(input("What is the Fahrenhite"))
DC = (DF - 32) * 5 /9
print("The Degree celcius is",DC)

#Alberto Benavides
#10-25-2021
#The number day of the week you will return on

day = int(input("How many days does the user leave"))
time = int(input("How many times does the user go out"))
w = (day + time)%7
print("The number of day of the week you will return on",w)