from assignment1_utils import (
    front_two_back_two,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
    min_max_sum
)


def test_front_two_back_two():
    assert front_two_back_two('') == ''
    assert front_two_back_two('a') == ''
    assert front_two_back_two('12') == '1212'
    assert front_two_back_two('123') == '1223'
    assert front_two_back_two('abcd') == 'abcd'
    assert front_two_back_two('0123456789') == '0189'
    assert front_two_back_two('Hello') == 'Helo'


def test_kelvin_to_celsius():
    assert kelvin_to_celsius(315.15) == 42.0
    assert kelvin_to_celsius(273.15) == 0.0


def test_kelvin_to_fahrenheit():
    assert kelvin_to_fahrenheit(315.15) == 107.6
    assert kelvin_to_celsius(273.15) == 0.0
    assert kelvin_to_fahrenheit(273.15) == 32.0


def test_min_max_sum():
    assert min_max_sum([1, 2, 3]) == [1, 3, 6]

    result = min_max_sum([12, 98, 23, 74, 3, 54])
    assert result[0] == 3
    assert result[1] == 98


print(max('AABABBACBAABCD'))
