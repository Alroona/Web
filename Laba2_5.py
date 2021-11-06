def isprime(number: int):

    for i in range(2,  number//2, 1):
        if number % i == 0:
            return False
    return True


num = int(input("Enter number: "))  # исходное число
print(isprime(num))
