import doctest
import unittest
import pytest


def get_number(number: int, mod: int = 10) -> str:
    """
    Функция получает целое число, систему исчисления и возвращает его  строковое представление.
    :param number: число
    :param mod: система исчисления
    :return: строковое представление
    >>> get_number(123, 2)
    '1111011'
    >>> get_number(123, 8)
    '173'
    """
    result = ''
    while number != 0:
        result = str(number % mod) + result
        number //= mod
    return result


class TestCaseNumbers(unittest.TestCase):
    def test_2(self):
        self.assertEqual(get_number(123, 2), '1111011', msg='Test failed')

    def test_3(self):
        self.assertEqual(get_number(123, 8), '173', msg='Test failed')


def test_2():
    assert get_number(123, 2) == '1111011', 'Test failed'


def test_3():
    assert get_number(123, 8) == '173', 'Test failed'




if __name__ == '__main__':


    doctest.testmod(verbose=True)
    unittest.main(verbosity=2)
    pytest.main(['-v'])