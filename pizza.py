#pizza.py
#This program calculates the cost per square inch of a pizza.

import math

def main():
    diameter = eval(input("Enter the diameter of the pizza: "))

    cost = eval(input("Enter the cost of the pizza: "))

    radius = diameter/2

    r = (radius*radius)                

    area = (3.14 * r)

    price = (cost/area)

    print("The cost of the pizza is", price,"per square inch")

main()
