import modules as m
calcType = input("What operation would you like to do? Type 1 for graphs, 2 for basic operations such as addition and subtraction, or 3 for algebraic equations. ")
if calcType == "1":
    m.graph()
elif calcType == "2":
    m.basicTingz()
elif calcType == "3":
    m.algebra()
