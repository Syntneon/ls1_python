
from python_lession import (is_odd, is_prime, is_arifm_progression, get_triangle_kind, is_palindrom, get_words, get_person_short_name, is_list_growing, get_pairs_number)

# -------------------------Задача 1-------------------------

def test_is_odd_with_even_number():
  
    "Тест на четное число."
    assert is_odd(4) is True


def test_is_odd_with_odd_number():
    "Тест на нечетное число."
    assert is_odd(5) is False


def test_is_odd_with_zero():
    "Тест на ноль."
    assert is_odd(0) is True


def test_is_odd_with_negative_even_number():
    "Тест на отрицательное четное число."
    assert is_odd(-10) is True


def test_is_odd_with_negative_odd_number():
    "Тест на отрицательное нечетное число."
    assert is_odd(-7) is False

#-------------------------Задача 2-------------------------

def test_is_simple_number():
    "Тест на простое число."
    assert is_prime(2) is True


def test_is_comp_number():
    "Тест на составное число."
    assert is_prime(4) is False


def test_is_simple_two_digit_number():
    "Тест на простое двузначное число."
    assert is_prime(31) is True


def test_is_comp_two_digit_number():
    "Тест на составное двузначное число."
    assert is_prime(98) is False

#-------------------------Задача 3-------------------------

def test_is_arifm_progression():
    "Тест на арифметическую прогрессию."
    assert is_arifm_progression(2, 4, 6) is True


def test_is_not_arifm_progression():
    "Тест на арифметическую прогрессию."
    assert is_arifm_progression(2, 4, 8) is False

#-------------------------Задача 4-------------------------

def test_equilateral_triangle():
    "Тест на равносторонний треугольник."
    assert get_triangle_kind(2, 2, 2) == "равносторонний"


def test_isosceles_triangle():
    "Тест на равнобедренный треугольник."
    assert get_triangle_kind(2, 2, 3) == "равнобедренный"


def test_triangle():
    "Тест на обычный треуголльник."
    assert get_triangle_kind(2, 4, 3) == "обычный"

#-------------------------Задача 5-------------------------

def test_is_palindrom():
    "Тест на палиндром."
    assert is_palindrom("топот") is True


def test_is_not_palindrom():
    "Тест на палиндром."
    assert is_palindrom("успех") is False

#-------------------------Задача 6-------------------------

def test_split_str():
    "Тест на разбиение строки"
    assert get_words("Александр Сергеевич Пушкин") == ["Александр", "Сергеевич", "Пушкин"]

#-------------------------Задача 7-------------------------

def test_get_person_short_name():
    "Тест на преобразование имени и отчества в инициалы"
    assert get_person_short_name("Лермонтов Михаил Юрьевич") == "Лермонтов М. Ю."

#-------------------------Задача 8-------------------------

def test_is_list_growing_true():
    "Тест на проверку, является ли список возрастающим"
    assert is_list_growing([1, 2, 3, 5, 7]) is True


def test_is_list_growing_false():
    "Тест на проверку, является ли список не возрастающим"
    assert is_list_growing([1, 2, 5, 3, 7]) is False

#-------------------------Задача 9-------------------------

def test_get_pairs_with_sum():
    "Тест на поиск пар значений которые в сумме составляют заданное число"
    assert get_pairs_number([1, 2, 4, 3, 5, 2], 7) == [(4,3), (5,2)]

def test_get_pairs_with_sum_duplicates():
    "Тест на поиск пар значений которые в сумме составляют заданное число"
    assert get_pairs_number([1, 2, 4, 3, 5, 2, 1, 1], 2) == [(1, 1)]
