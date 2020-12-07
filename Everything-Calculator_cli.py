from matplotlib.pyplot import *
from numpy import *
from sympy.solvers import solve
from sympy import Symbol

def graph():
    graphType = input("What kind of graph would you like: linear, quadratic, cubic, or quartic? Type 1 for linear, 2 for quadratic, 3 for cubic, or 4 for quartic. ")
    if graphType == "1":
        range1 = int(input("What is the first number of the range? "))
        range2 = int(input("What is the second number of the range? "))
        m = int(input("What is the value of the slope, or the variable m in the equation y = mx + b? "))
        b = int(input("What is the value of the y-intercept, or the variable b in the equation y = mx + b? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y=m*x+b
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
    elif graphType == "2":
        formatType = input("What format woud you like to enter the values for the function: ax^2 + bx + c or a(x - h)^2 + k? Type 1 for the first option or 2 for the second option. ")
        range1 = int(input("What is the first number of the range? "))
        range2 = int(input("What is the second number of the range? "))
    if formatType == "1":
        a = int(input("What is the value of the variable a in the equation y = ax² + bx + c? "))
        b = int(input("What is the value of the variable b in the equation y = ax² + bx + c? "))
        c = int(input("What is the value of the variable c in the equation y = ax² + bx + c? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = (x**2)*a+(b*x)+c
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
    elif formatType == "2":
        a = int(input("What is the value of the variable a in the equation y = a(x - h)² + k? "))
        h = int(input("What is the value of the variable h in the equation y = a(x - h)² + k? "))
        k = int(input("What is the value of the variable k in the equation y = a(x - h)² + k? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = (a*((x - h)**2))+k
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
    elif graphType == "3":
        formatType = input("What format woud you like to enter the values for the function: ax³ + bx² + cx + d, a(x - h)³ + k, a(x-α)(x-β)(x-γ) or a(x-α)²(x-β)? Type 1 for the first option, 2 for the second option, 3 for the third option or 4 for the fourth option. ")
    range1 = int(input("What is the first number of the range? "))
    range2 = int(input("What is the second number of the range? "))
    if formatType == "1":
        a = int(input("What is the value of the variable a in the equation y = ax³ + bx² + cx + d? "))
        b = int(input("What is the value of the variable b in the equation y = ax³ + bx² + cx + d? "))
        c = int(input("What is the value of the variable c in the equation y = ax³ + bx² + cx +d? "))
        d = int(input("What is the value of the variable d in the equation y = ax³ + bx² + cx + d? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = (x**3)*a+(x**2)*b+c*x+d
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
    if formatType == "2":
        a = int(input("What is the value of the variable a in the equation a(x - h)³ + k? "))
        h = int(input("What is the value of the variable h in the equation a(x - h)³ + k? "))
        k = int(input("What is the value of the variable k in the equation a(x - h)³ + k? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = (a*((x - h)**3))+k
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
    if formatType == "3":
        a = int(input("What is the value of the variable a in the equation a(x-α)(x-β)(x-γ)? "))
        aa = int(input("What is the value of the variable α in the equation a(x-α)(x-β)(x-γ)? "))
        bb = int(input("What is the value of the variable β in the equation a(x-α)(x-β)(x-γ)? "))
        y = int(input("What is the value of the variable γ in the equation a(x-α)(x-β)(x-γ)? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = a*(x-aa)*(x-bb)*(x-y)
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
    if formatType == "4":
        a = int(input("What is the value of the variable a in the equation a(x-α)²(x-β)? "))
        aa = int(input("What is the value of the variable α in the equation a(x-α)²(x-β)? "))
        bb = int(input("What is the value of the variable β in the equation a(x-α)²(x-β)? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = a*((x-aa)**2)*(x-bb)
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
    elif graphType == "4":
        formatType = input("What format would you like to enter the values for the function: ax⁴ + bx³ + cx² + dx + e, a(x - h)⁴ + k, a(x-α)(x-β)(x-γ)(x-δ), a(x-α)²(x-β)(x-γ), or a(x-α)³(x-β)? Type 1 for the first option, 2 for the second option, 3 for the third option, 4 for the fourth option, or 5 for the fifth option. ")
    range1 = int(input("What is the first number of the range? "))
    range2 = int(input("What is the second number of the range? "))
    if formatType == "1":
        a = int(input("What is the value of the variable a in the equation y = ax⁴ + bx³ + cx² + dx + e? "))
        b = int(input("What is the value of the variable b in the equation y = ax⁴ + bx³ + cx² + dx + e? "))
        c = int(input("What is the value of the variable c in the equation y = ax⁴ + bx³ + cx² + dx + e? "))
        d = int(input("What is the value of the variable d in the equation y = ax⁴ + bx³ + cx² + dx + e? "))
        e = int(input("What is the value of the variable e in the equation y = ax⁴ + bx³ + cx² + dx + e? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = (x**4)*a+(x**3)*b+(x**2)*c+d*x+c
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
    if formatType == "2":
        a = int(input("What is the value of the variable a in the equation a(x - h)⁴ + k? "))
        h = int(input("What is the value of the variable h in the equation a(x - h)⁴ + k? "))
        k = int(input("What is the value of the variable k in the equation a(x - h)⁴ + k? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = (a*((x - h)**4))+k
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
    if formatType == "3":
        a = int(input("What is the value of the variable a in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
        aa = int(input("What is the value of the variable α in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
        bb = int(input("What is the value of the variable β in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
        y = int(input("What is the value of the variable γ in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
        dd = int(input("What is the value of the variable δ in the equation a(x-α)(x-β)(x-γ)(x-δ)? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = a*(x-aa)*(x-bb)*(x-y)
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
    if formatType == "4":
        a = int(input("What is the value of the variable a in the equation a(x-α)²(x-β)(x-γ)? "))
        aa = int(input("What is the value of the variable α in the equation a(x-α)²(x-β)(x-γ)? "))
        bb = int(input("What is the value of the variable β in the equation a(x-α)²(x-β)(x-γ)? "))
        y = int(input("What is the value of the variable γ in the equation a(x-α)²(x-β)(x-γ)? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = a*((x-aa)**2)*(x-bb)*(x-y)
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
    if formatType == "5":
        a = int(input("What is the value of the variable a in the equation a(x-α)³(x-β)? "))
        aa = int(input("What is the value of the variable α in the equation a(x-α)³(x-β)? "))
        bb = int(input("What is the value of the variable β in the equation a(x-α)³(x-β)? "))
        y = int(input("What is the value of the variable γ in the equation a(x-α)³(x-β)? "))
        x=linspace(range1,range2,5000)
        ylim([-50,50])
        y = a*((x-aa)**3)*(x-bb)
        plot(x,y)
        grid(b=True, which='major', color='#666666', linestyle='-')
        show()
def basicTingz():
    optType = input("What operation would you like to do? Press 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division. ")
    if optType == "1":
        equation = input("Input your equation here (Make sure to use this sign \"+\" for addition!): ")
        solution = eval(equation)
        print(solution)
    elif optType == "2":
        equation = input("Input your equation here (Make sure to use this sign \"-\" for subtraction!): ")
        solution = eval(equation)
        print(solution)
    elif optType == "3":
        equation = input("Input your equation here (Make sure to use this sign \"*\" for multiplication!): ")
        solution = eval(equation)
        print(solution)
    elif optType == "4":
        equation = input("Input your equation here (Make sure to use this sign \"/\" for multiplication!): ")
        solution = eval(equation)
        print(solution)
calcType = input("What operation would you like to do? Type 1 for graphs, or 2 for basic operations such as addition and subtraction.")
if calcType == "1":
    graph()
elif calcType == "2":
    basicTingz()
