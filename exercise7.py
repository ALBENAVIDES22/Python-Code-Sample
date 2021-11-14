#Alberto Benavides
#11-13-2021
#Write a Python function to check whether a number is in a given range

import math

def areaOfCircle(r):
    area = math.pi * r**2
    return area

#Alberto Benavides
#11-13-2021
#Write a Python function to check whether a number is in a given range.
#Use range (1, 10) Print whether the number is in or not in the range
def rangeCheck(num):
    #evaluate the number is in the range
    #     in range (1, 10)
    if num in range (1, 10):
       print("In range")
    else:
       print("Not in range")

n = int(input("Enter a number:"))
rangeCheck(n)

#Alberto Benavides
#11-13-2021
#Write a Python function to multiply all the numbers in a list. Use list [5, 2, 7, -1]


def multiplyList(L):
    total = 1
    #iterate each number in the list
    for i in L:
        total = total * i
    return total

numL = [5, 2, 7, -1]
print("total is", multiplyList(numL))

#Alberto Benavides
#11-13-2021
#Write a Python function that takes a list of numbers and returns a new list with unique
#elements of the first list. Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function.
#def uniqueL(L):

def unique_list(l):
 x = []
 for a in l:
        if a not in x:
            x. append(a)
            return x
        print [1, 3, 3, 3, 6, 2, 3, 5]

#Alberto Benavides
#11-13-2021
#Use the following chunk of code as a base to produce the image shown below

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range (4):
        t.forward(sz)
        t.left (90)

    wn = turtle.Screen()

    alex =turtle.Turtle()
    alex.color ("black")

    wn.exitonclick()

#Alberto Benavides
#11-13-2021
#Make Python car

class car:

    def _init_(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
    def get_model(self):
        return self.model
    def get_color(self):
        return self.color
    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color
car1 = car("Sports", 2012, "Blue")
car2 = car("Sedan", 2020, "Black")

print(car1.get_color("Blue"))
print(car1.get_model("Sports"))
print(car2.get_color("Black"))
print(car1.fullspecs("2012"))
print(car2.fullspecs("2020"))
