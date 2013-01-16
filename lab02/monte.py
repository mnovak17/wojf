#monte.py
#calculates value of pi with random dart throw simulation
#Mitch Novak
#1/11/13

import random
import math

def main():
    print("This program calculates the value of Pi by \nsimulating the throwing of darts ont a round \ntarget on a square background.")
    print()
    throws = eval(input("How many darts to throw?"))
    hits = 0
    for i in range(0, throws):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        distance = simpleDistance(x,y)
        if (distance <= 1):
            hits = hits + 1
    print("The value of Pi after", throws, "iterations is", 4* (hits/throws))

def simpleDistance(x, y):
    return math.sqrt(x*x + y*y)


main()