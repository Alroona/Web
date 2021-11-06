cache_argument = 0
cache_result = False


def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1):  # аргументы прибывают отсюда
        global cache_argument
        global cache_result
        if cache_argument == arg1:
            print(cache_result)
        else:
            cache_argument = arg1
            cache_result = function_to_decorate(arg1)
            print(cache_result)

    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def is_prime(arg):
    if arg < 0: return False
    print("Entering prime")   # Демонстрация входа в функцию
    for i in range(2, arg // 2, 1):
        if arg % i == 0:
            return False
    return True


number = 0

while number != -1:  # Выход из цикла по вводу -1 в консоль
    number = int(input("Enter number: "))
    is_prime(number)
