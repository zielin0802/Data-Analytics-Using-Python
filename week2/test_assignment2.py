from assignment2 import fib, get_element, set_operation, sum_tuples, to_binary_recursion


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(9) == 34


def test_get_element():
    in_tuple = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
    assert get_element(in_tuple) == ('e', 'u')


def test_set_operation():
    assert set_operation({1, 2}, {1, 2, 3}) == 'yes'
    assert set_operation({1, 3, 4, 5}, {2, 4, 6, 8}) == 'no'


def test_sum_tuples():
    in1 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
    expected = [9, -1, 7, 8]
    actual = sum_tuples(in1)
    assert actual == expected
    assert type(actual) is list

    in2 = [(), (1, 2), (2, 3), (3, 4)]
    expected = [0, 3, 5, 7]
    actual = sum_tuples(in2)
    assert actual == expected
    assert type(actual) is list


def test_to_binary_recursion():
    assert to_binary_recursion(0) == '0'
    assert to_binary_recursion(1) == '1'
    assert to_binary_recursion(2) == '10'
    assert to_binary_recursion(3) == '11'
    assert to_binary_recursion(4) == '100'
    assert to_binary_recursion(5) == '101'
    assert to_binary_recursion(6) == '110'
    assert to_binary_recursion(7) == '111'
    assert to_binary_recursion(8) == '1000'
