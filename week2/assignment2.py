def fib(n):
    if n < 0:
        return 'Undefined'
    elif n == 0:
        return 0
    elif n in (1, 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def get_element(tuple):
    return (tuple[3], tuple[-4])


def set_operation(A, B):
    return 'yes' if A.issubset(B) else 'no'


def sum_tuples(my_tuple):
    return [sum(t) for t in my_tuple]


def to_binary_recursion(n):
    if n == 0:
        return "0"

    q = int(to_binary_recursion(n // 2))
    remainder = n % 2

    return str(remainder + 10 * q)
