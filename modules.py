from matplotlib.pyplot import *
from numpy import *
from math import *
import sys
#Graph Function
def graph():
    graphType = input("What kind of graph would you like? Here are the options: \n Type 1 for linear, \n 2 for quadratic, \n 3 for cubic, \n or 4 for quartic.\n\n Please type the corresponding number of the operation you would like to do: ")
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
        formatType = input("What format woud you like to enter the values for the function: ax^2 + bx + c or a(x - h)^2 + k? Type 1 for the first option or 2 for the second option. ")
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
    elif graphType == "3":
        formatType = input("What format woud you like to enter the values for the function: ax³ + bx² + cx + d, a(x - h)³ + k, a(x-α)(x-β)(x-γ) or a(x-α)²(x-β)? Type 1 for the first option, 2 for the second option, 3 for the third option or 4 for the fourth option. ")
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
    if formatType == "2":
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
    if formatType == "3":
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
    if formatType == "4":
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
    elif graphType == "4":
        formatType = input("What format would you like to enter the values for the function: ax⁴ + bx³ + cx² + dx + e, a(x - h)⁴ + k, a(x-α)(x-β)(x-γ)(x-δ), a(x-α)²(x-β)(x-γ), or a(x-α)³(x-β)? Type 1 for the first option, 2 for the second option, 3 for the third option, 4 for the fourth option, or 5 for the fifth option. ")
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
        y = (x**4)*a+(x**3)*b+(x**2)*c+d*x+c
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
        sys.exit()
    if formatType == "2":
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
    if formatType == "3":
        a = float(input("What is the value of the variable a in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
        aa = float(input("What is the value of the variable α in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
        bb = float(input("What is the value of the variable β in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
        y = float(input("What is the value of the variable γ in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
        dd = float(input("What is the value of the variable δ in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = a*(x-aa)*(x-bb)*(x-y)
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
        sys.exit()
    if formatType == "4":
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
    if formatType == "5":
        a = float(input("What is the value of the variable a in the equation a(x-α)³(x-β)? "))
        aa = float(input("What is the value of the variable α in the equation a(x-α)³(x-β)? "))
        bb = float(input("What is the value of the variable β in the equation a(x-α)³(x-β)? "))
        y = float(input("What is the value of the variable γ in the equation a(x-α)³(x-β)? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = a*((x-aa)**3)*(x-bb)
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
        sys.exit()
# Basic Operations
def basicTingz():
    optType = input("What operation would you like to do? Press 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division. ")
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
# Algebraicequatiobs
def algebra():
    equType = input("What type of equation would you like to solve? Type for a first degree equation in the form of ax + b = cx + d, or 2 for a quadratic equation for ax^2 + bx + c  = 0. ")
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
# Area calculations
def area():
    shape = input("What Shape would you like to calculate the area of? Type 1 for circle, 2 for triangle and 3 for square and rectangle")
    if shape == "1":
        r = float(input("Input the radius of the circle : "))
        print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
    elif shape == "2":
        type  = input("Type 1 for calculating the area of the triangle with the length of the 3 sides, or 2 for calculating the area of the triangle with the base and the height. ")
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



# def exit():
  #  ans = input("Would you like to continue? ")
  #  if ans == "y":
