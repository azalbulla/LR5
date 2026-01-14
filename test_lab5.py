import pytest
import random
from lab5_functions import *


# Фикстура 1: тестовые числа
@pytest.fixture
def numbers():
    return [1, -3, 6, -9, 3, 80, 35, -42, 90, -5]


# Фикстура 2: данные для сортировки
@pytest.fixture
def data():
    return [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]


# Тест 1: четные числа
def test_is_even():
    assert is_even(4) == True
    assert is_even(3) == False
    assert is_even(0) == True


# Тест 2: НОД
def test_gcd():
    assert gcd(10, 5) == 5
    assert gcd(7, 15) == 1
    assert gcd(48, 18) == 6


# Тест 3: сумма положительных
def test_sum_positive():
    assert sum_positive([1, -2, 3]) == 4
    assert sum_positive([]) == 0
    assert sum_positive([-1, -2, -3]) == 0


# Тест с фикстурой
def test_sum_with_fixture(numbers):
    assert sum_positive(numbers) == 215


# Параметризованный тест
@pytest.mark.parametrize("num, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
    (15, False)
])
def test_even_numbers(num, expected):
    assert is_even(num) == expected


# Тест 4: перевод в систему счисления
def test_convert_base():
    assert convert_base(12, 2) == "1100"
    assert convert_base(255, 16) == "ff"
    assert convert_base(0, 2) == "0"


# Тест 5: палиндром
def test_is_palindrome():
    assert is_palindrome("казак") == True
    assert is_palindrome("python") == False
    assert is_palindrome("А роза упала на лапу Азора") == True

@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 5),
    (7, 15, 1),
    (48, 18, 6),
    (100, 50, 50),
    (17, 17, 17),
    (0, 5, 5),
    (-10, 5, 5),
])
def test_gcd_param(a, b, expected):
    assert gcd(a, b) == expected


# Тесты сортировок
def test_bubble_sort(data):
    result = bubble_sort(data)
    assert result == sorted(data)


def test_selection_sort(data):
    result = selection_sort(data)
    assert result == sorted(data)


def test_insertion_sort(data):
    result = insertion_sort(data)
    assert result == sorted(data)


def test_merge_sort(data):
    result = merge_sort(data)
    assert result == sorted(data)


# Тестирование на пустом массиве
def test_empty_sort():
    for sort_func in [bubble_sort, selection_sort, insertion_sort, merge_sort]:
        result = sort_func([])
        assert result == []


# Тестирование на одном элементе
def test_single_sort():
    for sort_func in [bubble_sort, selection_sort, insertion_sort, merge_sort]:
        result = sort_func([5])
        assert result == [5]


# Тестирование уже отсортированного массива
def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    for sort_func in [bubble_sort, selection_sort, insertion_sort, merge_sort]:
        result = sort_func(arr)
        assert result == [1, 2, 3, 4, 5]


# Тестирование обратного массива
def test_reverse_array():
    arr = [5, 4, 3, 2, 1]
    for sort_func in [bubble_sort, selection_sort, insertion_sort, merge_sort]:
        result = sort_func(arr)
        assert result == [1, 2, 3, 4, 5]


# Тест с отрицательными числами
def test_negative_numbers():
    arr = [-5, -1, -3, -2, -4]
    for sort_func in [bubble_sort, selection_sort, insertion_sort, merge_sort]:
        result = sort_func(arr)
        assert result == sorted(arr)


# Тест со случайными данными
def test_random_data():
    arr = [random.randint(-100, 100) for _ in range(20)]
    for sort_func in [bubble_sort, selection_sort, insertion_sort, merge_sort]:
        result = sort_func(arr)
        assert result == sorted(arr)


# Медленный тест (маркировка)
@pytest.mark.slow
def test_big_array():
    arr = [random.randint(-1000, 1000) for _ in range(300)]
    result = merge_sort(arr)
    assert result == sorted(arr)


# Интеграционный тест
def test_sort_and_gcd():
    arr = [48, 18, 32, 12, 24]
    sorted_arr = bubble_sort(arr)

    current_gcd = sorted_arr[0]
    for num in sorted_arr[1:]:
        current_gcd = gcd(current_gcd, num)

    assert current_gcd == 2


# Проверка что сортировка не меняет оригинал
def test_original_not_changed():
    original = [3, 1, 4, 1, 5]
    original_copy = original[:]

    bubble_sort(original)
    assert original == original_copy
