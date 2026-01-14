# 1. Проверка четности числа
def is_even(num):
    return num % 2 == 0


# 2. Наибольший общий делитель
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


# 3. Сумма положительных чисел
def sum_positive(nums):
    total = 0
    for num in nums:
        if num > 0:
            total += num
    return total


# 4. Перевод в систему счисления
def convert_base(x, base):
    if x == 0:
        return '0'
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    while x != 0:
        result = digits[x % base] + result
        x //= base
    return result


# 5. Проверка палиндрома
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


# Сортировки из лабораторной работы 3
def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
