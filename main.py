import modules as m
calcType = input("What operation would you like to do?  Here are the options:\n 1 for graphs,\n 2 for basic operations such as addition and subtraction,\n 3 for algebraic equations, or\n 4 for area.\n\nPlease type the corresponding number of the operation you would like to do:   ")
if calcType == "1":
    m.graph()
elif calcType == "2":
    m.basicTingz()
elif calcType == "3":
    m.algebra()
elif calcType == "4":
    m.area()

