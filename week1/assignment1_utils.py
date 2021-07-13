# 1
def front_two_back_two(input_string):
    return '' if len(input_string) < 2 else input_string[:2] + input_string[-2:]


# 2
def kelvin_to_celsius(k):
    return k - 273.15


# 2
def kelvin_to_fahrenheit(k):
    return kelvin_to_celsius(k) * 9.0 / 5.0 + 32.0


# 4
def min_max_sum(input_list):
    return [min(input_list), max(input_list), sum(input_list)]


# 5
def print_square():
    squares_map = {base: base * base for base in range(1, 16)}
    print(squares_map)
