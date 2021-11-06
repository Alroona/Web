def palindrom(x: int) -> int:

    x_reversed = str(x)[::-1]

    if str(x) == str(x_reversed):
        return True
    else:
        return False


a = int(input("Enter number "))
print(palindrom(a))