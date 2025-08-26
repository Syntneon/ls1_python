# pylint: skip-file

# -------------- Arifmetic operations --------------

"""
Напишите функцию, которая возвращает true, если число является четным.
Подсказка: используйте % для определения остатка от деления: 10 % 3 = 1
"""


def is_odd(n: int) -> bool:

    if (n % 2 == 0):
        return True
    else:
        return False


"""
Напишите функцию, которая возращает true, если число является простым
"""


def is_prime(n: int) -> bool:

    if (n  <= 1):
        return False

    for i in range(2, n):
        if ( n % i == 0):
            return False

    return True
    


"""
Напишите функцию, которая возвращает true, если
три заданных числа (в указанном порядке) являются последовательными членами
арифметической прогрессии
"""


def is_arifm_progression(a: int, b: int, c: int) -> bool:

    if (c - b == b - a):
        return True

    return False


# -------------- If condition --------------

"""
    Напишите функцию, которая принимает три положительных числа и 
    возвращает вид треугольника (равносторонний, равнобедренный, обычный).
"""


def get_triangle_kind(a: int, b: int, c: int) -> str:

    if (a == b == c):
        return "равносторонний"
    elif (a == b or b == c or a == c):
        return "равнобедренный"
    return "обычный"


# -------------- strings, for loops --------------
"""
    Проверить, является ли строка с пробелами палиндромом (а роза упала на лапу азора).
    Упростим задачу, допуская, что cлова в предложении разделяются только одним пробелом.
"""


def is_palindrom(s: str) -> bool:

    s_clean = s.replace(' ', '').lower()
    return s_clean == s_clean[::-1]
    

"""
    Дана строка, разбить ее на слова. Слова разделены одним пробелом
    "Александр Сергеевич Пушкин" -> ["Александр", "Сергеевич", "Пушкин"]
"""


def get_words(s: str) -> list[str]:
    return s.split()


"""
    Дана ФИО, напишите функцию, которая выводит фамилию и инициалы через точку.
    Например: "Лермонтов Михаил Юрьевич" -> "Лермонтов М. Ю."
"""


def get_person_short_name(fio: str) -> str:
   
    parts = fio.split()

    last_name = parts[0]
    first_name = parts[1]
    surname = parts[2]
   
    return f"{last_name} {first_name[0]}. {surname[0]}."


# -------------- lists --------------

"""
    Напишите функцию, которая вернет true, если список является полностью возрастающим,
    т.е. каждый следующий элемент больше предыдущего
"""


def is_list_growing(lst: list[float]) -> bool:

    for i in range(1, len(lst)):
        if lst[i] <= lst[i-1]:
            return False

    return True


"""
    Дан список целых чисел и определенное заданное число. Найти все пары из списка,
    сумма которых равна этому числу.
    Верните из функции список кортежей.
    Например: get_pairs_number([1, 2, 4, 3, 5, 2], 7) -> [(4,3), (5,2)]
"""

def get_pairs_number(lst: list[int], n) -> list[tuple]:

    pairs = []
    
    for i in range(1, len(lst)):
        if lst[i] + lst[i-1] == n:
            pairs.append((lst[i-1], lst[i]))
            
    return pairs
