def palindrom(x: int) -> int:

    x_reversed = str(x)[::-1]
    if x_reversed[-1] == '-':
        x_reversed = x_reversed[:-1]
        x_reversed = '-' + x_reversed
        return int(x_reversed)
    else:
        return int(x_reversed)


num = int(input("Enter number "))
print(palindrom(num))
