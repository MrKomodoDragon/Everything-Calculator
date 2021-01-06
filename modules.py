# pylint: disable=unused-wildcard-import, method-hidden, 
# pylint: enable=too-many-lines
from matplotlib.pyplot import *
from numpy import *
from math import *
import sys
CRED = '\033[91m'
CEND = '\033[0m'
#Graph Function
def graph():
    graphType = input("What kind of graph would you like? Here are the options: \n Type 1 for linear, \n 2 for quadratic, \n 3 for cubic, \n or 4 for quartic.\n\n Please type the corresponding number of the graph you would like to do: ")
    # Linear Graph
    if graphType == "1":
        range1 = float(input("What is the first number of the range? "))
        range2 = float(input("What is the second number of the range? "))
        m = float(input("What is the value of the slope, or the variable m in the equation y = mx + b? "))
        b = float(input("What is the value of the y-intercept, or the variable b in the equation y = mx + b? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y=m*x+b
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
        sys.exit()
    # Quadratic Graph
    elif graphType == "2":
        formatType = input("What format woud you like to enter the values for the function? Here are the options:\n 1 for ax^2 + bx + c, or\n 2 for a(x - h)^2 + k?\n Please type the corresponding number of the format you would like to do:  ")
        range1 = float(input("What is the first number of the range? "))
        range2 = float(input("What is the second number of the range? "))
        if formatType == "1":
            a = float(input("What is the value of the variable a in the equation y = ax² + bx + c? "))
            b = float(input("What is the value of the variable b in the equation y = ax² + bx + c? "))
            c = float(input("What is the value of the variable c in the equation y = ax² + bx + c? "))
            x=linspace(range1,range2,5000)
            ylim([-50,50])
            y = (x**2)*a+(b*x)+c
            plot(x,y)
            grid(b=True, which='major', color='#666666', linestyle='-')
            show()
            sys.exit()
        elif formatType == "2":
            a = float(input("What is the value of the variable a in the equation y = a(x - h)² + k? "))
            h = float(input("What is the value of the variable h in the equation y = a(x - h)² + k? "))
            k = float(input("What is the value of the variable k in the equation y = a(x - h)² + k? "))
            x=linspace(range1,range2,5000)
            ylim([-50,50])
            y = (a*((x - h)**2))+k
            plot(x,y)
            grid(b=True, which='major', color='#666666', linestyle='-')
            show()
            sys.exit()
        else:
            print(CRED + "That was an invalid option. Please try again" + CEND)
    elif graphType == "3":
        formatType = input("What format woud you like to enter the values for the function? Here are the options:\n 1 for ax³ + bx² + cx + d,\n 2 for a(x - h)³ + k, \n 3 for a(x-α)(x-β)(x-γ), or\n 4 for a(x-α)²(x-β)\n Please type the corresponding number of the format you would like to do: ")
        range1 = float(input("What is the first number of the range? "))
        range2 = float(input("What is the second number of the range? "))
        if formatType == "1":
            a = float(input("What is the value of the variable a in the equation y = ax³ + bx² + cx + d? "))
            b = float(input("What is the value of the variable b in the equation y = ax³ + bx² + cx + d? "))
            c = float(input("What is the value of the variable c in the equation y = ax³ + bx² + cx +d? "))
            d = float(input("What is the value of the variable d in the equation y = ax³ + bx² + cx + d? "))
            x=linspace(range1,range2,5000)
            ylim([-50,50])
            y = (x**3)*a+(x**2)*b+c*x+d
            plot(x,y)
            grid(b=True, which='major', color='#666666', linestyle='-')
            show()
            sys.exit()
        elif formatType == "2":
            a = float(input("What is the value of the variable a in the equation a(x - h)³ + k? "))
            h = float(input("What is the value of the variable h in the equation a(x - h)³ + k? "))
            k = float(input("What is the value of the variable k in the equation a(x - h)³ + k? "))
            x=linspace(range1,range2,5000)
            ylim([-50,50])
            y = (a*((x - h)**3))+k
            plot(x,y)
            grid(b=True, which='major', color='#666666', linestyle='-')
            show()
            sys.exit()
        elif formatType == "3":
            a = float(input("What is the value of the variable a in the equation a(x-α)(x-β)(x-γ)? "))
            aa = float(input("What is the value of the variable α in the equation a(x-α)(x-β)(x-γ)? "))
            bb = float(input("What is the value of the variable β in the equation a(x-α)(x-β)(x-γ)? "))
            y = float(input("What is the value of the variable γ in the equation a(x-α)(x-β)(x-γ)? "))
            x=linspace(range1,range2,5000)
            ylim([-50,50])
            y = a*(x-aa)*(x-bb)*(x-y)
            plot(x,y)
            grid(b=True, which='major', color='#666666', linestyle='-')
            show()
            sys.exit()
        elif formatType == "4":
            a = float(input("What is the value of the variable a in the equation a(x-α)²(x-β)? "))
            aa = float(input("What is the value of the variable α in the equation a(x-α)²(x-β)? "))
            bb = float(input("What is the value of the variable β in the equation a(x-α)²(x-β)? "))
            x=linspace(range1,range2,5000)
            ylim([-50,50])
            y = a*((x-aa)**2)*(x-bb)
            plot(x,y)
            grid(b=True, which='major', color='#666666', linestyle='-')
            show()
            sys.exit()
        else:
            print(CRED + "That was an invalid option. Please try again" + CEND)
    elif graphType == "4":
        formatType = input("What format would you like to enter the values for the function? Here are the options: \n 1 for ax⁴ + bx³ + cx² + dx + e, \n 2 for a(x - h)⁴ + k, \n  3 for a(x-α)(x-β)(x-γ)(x-δ), \n 4 for a(x-α)²(x-β)(x-γ), or \n 5 for a(x-α)³(x-β)? \n Please type the corresponding number of the format you would like to do:  ")
        range1 = float(input("What is the first number of the range? "))
        range2 = float(input("What is the second number of the range? "))
        if formatType == "1":
            a = float(input("What is the value of the variable a in the equation y = ax⁴ + bx³ + cx² + dx + e? "))
            b = float(input("What is the value of the variable b in the equation y = ax⁴ + bx³ + cx² + dx + e? "))
            c = float(input("What is the value of the variable c in the equation y = ax⁴ + bx³ + cx² + dx + e? "))
            d = float(input("What is the value of the variable d in the equation y = ax⁴ + bx³ + cx² + dx + e? "))
            e = float(input("What is the value of the variable e in the equation y = ax⁴ + bx³ + cx² + dx + e? "))
            x=linspace(range1,range2,5000)
            ylim([-50,50])
            y = (x**4)*a+(x**3)*b+(x**2)*c+d*x+e
            plot(x,y)
            grid(b=True, which='major', color='#666666', linestyle='-')
            show()
            sys.exit()
        elif formatType == "2":
            a = float(input("What is the value of the variable a in the equation a(x - h)⁴ + k? "))
            h = float(input("What is the value of the variable h in the equation a(x - h)⁴ + k? "))
            k = float(input("What is the value of the variable k in the equation a(x - h)⁴ + k? "))
            x=linspace(range1,range2,5000)
            ylim([-50,50])
            y = (a*((x - h)**4))+k
            plot(x,y)
            grid(b=True, which='major', color='#666666', linestyle='-')
            show()
            sys.exit()
        elif formatType == "3":
            a = float(input("What is the value of the variable a in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
            aa = float(input("What is the value of the variable α in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
            bb = float(input("What is the value of the variable β in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
            y = float(input("What is the value of the variable γ in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
            dd = float(input("What is the value of the variable δ in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
            x=linspace(range1,range2,5000)
            ylim([-50,50])
            y = a*(x-aa)*(x-bb)*(x-y)*(x-dd)
            plot(x,y)
            grid(b=True, which='major', color='#666666', linestyle='-')
            show()
            sys.exit()
        elif formatType == "4":
            a = float(input("What is the value of the variable a in the equation a(x-α)²(x-β)(x-γ)? "))
            aa = float(input("What is the value of the variable α in the equation a(x-α)²(x-β)(x-γ)? "))
            bb = float(input("What is the value of the variable β in the equation a(x-α)²(x-β)(x-γ)? "))
            y = float(input("What is the value of the variable γ in the equation a(x-α)²(x-β)(x-γ)? "))
            x=linspace(range1,range2,5000)
            ylim([-50,50])
            y = a*((x-aa)**2)*(x-bb)*(x-y)
            plot(x,y)
            grid(b=True, which='major', color='#666666', linestyle='-')
            show()
            sys.exit()
        elif formatType == "5":
            a = float(input("What is the value of the variable a in the equation a(x-α)³(x-β)? "))
            aa = float(input("What is the value of the variable α in the equation a(x-α)³(x-β)? "))
            bb = float(input("What is the value of the variable β in the equation a(x-α)³(x-β)? "))
            x=linspace(range1,range2,5000)
            ylim([-50,50])
            y = a*((x-aa)**3)*(x-bb)
            plot(x,y)
            grid(b=True, which='major', color='#666666', linestyle='-')
            show()
            sys.exit()
        else:
            print(CRED + "That was an invalid option. Please try again" + CEND)
    else:
        print(CRED + "That was an invalid option. Please try again" + CEND)
        graph()
# Basic Operations
def basicTingz():
    optType = input("What operation would you like to do? Here are the options: \n 1 for addition, \n 2 for subtraction, \n 3 for multiplication, or \n 4 for division. \n  Please type the corresponding number of the operation you would like to do: ")
    if optType == "1":
        equation = input("Input your equation here (Make sure to use this sign \"+\" for addition!): ")
        solution = eval(equation)
        print(solution)
        sys.exit()
    elif optType == "2":
        equation = input("Input your equation here (Make sure to use this sign \"-\" for subtraction!): ")
        solution = eval(equation)
        print(solution)
        sys.exit()
    elif optType == "3":
        equation = input("Input your equation here (Make sure to use this sign \"*\" for multiplication!): ")
        solution = eval(equation)
        print(solution)
        sys.exit()
    elif optType == "4":
        equation = input("Input your equation here (Make sure to use this sign \"/\" for division!): ")
        solution = eval(equation)
        print(solution)
        sys.exit()
    else:
        print(CRED + "That was an invalid option. Please try again" + CEND)
        basicTingz()
# Algebraic Equations
def algebra():
    equType = input("What type of equation would you like to solve?  Here are the options: \n 1 for a first degree equation in the form of ax + b = cx + d, or \n 2 for a quadratic equation in the form of ax^2 + bx + c  = 0. Please type the corresponding number of the equation you would like to do:  ")
    if equType == "1":
       a = float(input("What is the value of a in ax + b = cx + d? "))
       b = float(input("What is the value of a in ax + b = cx + d? "))
       c = float(input("What is the value of a in ax + b = cx + d? "))
       d = float(input("What is the value of a in ax + b = cx + d? "))
       answer = (d - b)/(a - c)
       print(answer)
       sys.exit()
    elif equType == "2":
        a = float(input("Enter the coefficients of a: "))
        b = float(input("Enter the coefficients of b: "))
        c = float(input("Enter the coefficients of c: "))
        d = b**2-4*a*c  # discriminant
        if d < 0:
            print("This equation has no real solution")
        elif d == 0:
            x = (-b+math.sqrt(b**2-4*a*c))/2*a
            print("This equation has one solutions: "), x
        else:
            x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
            x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
            print("This equation has two solutions: ", x1, " or", x2)
    else:
        print(CRED + "That was an invalid option. Please try again" + CEND)
        algebra()
# Area calculations
def area():
    shape = input("What Shape would you like to calculate the area of? Here are the options: \n 1 for circle, \n 2 for triangle, or \n 3 for square and rectangle. \n Please type the corresponding number of the shape you would like to do:  ")
    if shape == "1":
        r = float(input("Input the radius of the circle : "))
        print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
    elif shape == "2":
        type = input("How would you like to calculate the area of the triangle? Here are the options: \n 1 for calculating the area of the triangle with the length of the 3 sides, \n or 2 for calculating the area of the triangle with the base and the height. \n Please type the corresponding number of the method you would like to do: ")
        if type == "2":
            base = float(input("What is the base of the Triangle? "))
            height = float(input("What is the height of the Triangle? "))
            area  = 0.5 * base * height
            print(area)
        elif type == "1":
            a = float(input("Length of first side: "))
            b = float(input("Length of second side: "))
            c = float(input("Length of third side: "))
            s = (a+b+c)/2
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
            print(area)
    elif shape == "3":
        l = float(input("Length of the Rectangle or square: "))
        w = float(input("width of the Rectangle or square: "))
        area  = l*w
        print(area)
    else:
        print(CRED + "That was an invalid option. Please try again" + CEND)
        area()



# def exit():
  #  ans = input("Would you like to continue? ")
  #  if ans == "y":
