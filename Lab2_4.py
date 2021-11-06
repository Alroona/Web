def nutonroot(number: float, rootdegree: int):

    root = number/rootDegree  # предположительное X0
    eps = 0.01   # точность
    rn = number
    while abs(root-rn) >= eps:
        rn = number
        iteration = 1
        while iteration < rootdegree:
            rn = rn/root
            iteration = iteration+1
        root = 0.5*(rn+root)
    return root


num = float(input("Enter number: "))  # исходное число
rootDegree = int(input("Enter root degree: "))  # степень корня
print(round(nutonroot(num, rootDegree), 3))
