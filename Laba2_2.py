def listdel(list_ent):
    a = []
    b = []
    c = []

    for num in list_ent:
        if num  % 2 == 0:
           a.append(num)
        if num % 3 == 0:
            b.append(num)
        if num % 5 == 0:
            c.append(num)
    print('A: ', a)
    print('B: ', b)
    print('C: ', c)


list_ent = []
for element in input("Enter number ").split():
    list_ent.append(int(element))

listdel(list_ent)