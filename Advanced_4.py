# 1. Написать функцию, которая будет принимать на вход натуральное число n, и возращать сумму его цифр.
# Реализовать используя рекурсию (без циклов, без строк, без контейнерных типов данных).
# Пример: get_sum_of_components(123) -> 6 (1+2+3)


def get_sum_of_components(number):
    if number == 0:
        return 0
    else:
        return number % 10 + get_sum_of_components(number // 10)


print(get_sum_of_components(0))

# 2. Написать декоратор log, который будет выводить на экран все аргументы, которые передаются вызываемой функции.
# @log
# def my_sum(*args):
# return sum(*args)


def log(func):

    def wrapper(*args):
        print(f'"Функция была вызвана с - {args}"')
        return_value = func(*args)
        return return_value
    return wrapper


@log
def my_sum(*args):
    return sum(args)


my_sum(1, 2, 3)

