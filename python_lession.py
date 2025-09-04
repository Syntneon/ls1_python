
"""
    Дан список целых чисел и определенное заданное число. Найти все пары из списка,
    сумма которых равна этому числу.
    Верните из функции список кортежей.
    Например: get_pairs_number([1, 2, 4, 3, 5, 2], 7) -> [(4,3), (5,2)]
"""

def get_pairs_of_numbers(lst: list[int], target_sum: int) -> list[tuple[int, int]]:
    seen = set()        
    pairs_lst = []          
    
    for num in lst:
        target = target_sum - num
        if target in seen:
            pair = tuple(sorted((target, num), reverse=True)) 
            if not pair in pairs_lst:
                pairs_lst.append(pair)
        seen.add(num)
    
    return pairs_lst




"""
    Нужно реализовать надпись в формате "N просмотров". Падеж слова "просмотр" зависит
    от числа N. Например, 1 просмотр, 2 просмотра и т.п.
"""


def get_views_count(n: int) -> str:
    
    word = ""

    if 11 <= n % 100 <= 14:
        word = "просмотров"

    else:
        last_digit = n % 10
        if last_digit == 1:
            word = "просмотр"
        elif 2 <= last_digit <= 4:
            word = "просмотра"
        else:
            word = "просмотров"

    return f"{n} {word}"


"""
    Дан список, содержащий нули. Вернуть список, где все нули сдвинты вправо,
    сохранив порядок исходного списка:
    move_zeros([1, 0, 0, 2, 3, 0, 1]) -> [1, 2, 3, 1, 0, 0, 0]

    Решить в двух вариантах:
    - функция принимаем список и возвращает НОВЫЙ список
    - функция изменяет список, который был передан в аргументе функции 
    (функция ничего не возвращает)
    
"""


def move_zeros(lst: list[float]) -> list:

    natural_numbers = [num for num in lst if num > 0]
    zeros = [num for num in lst if num == 0]

    return natural_numbers + zeros



def move_zeros_2(lst: list[float]) -> list:
    lst.sort(key = lambda x: x == 0)
    print(lst)


"""
    Данные загрузились из БД с лишними символами, а должны быть только русские буквы.
    Напишите функцию, которая удаляет символы, которые не являются русскими буквами.
    "Иsвtrан Ив^%ан Ива?но)вич" -> "Иванов Иван Иванович"
"""


def clean_name(fio: str) -> str:

    clean_fio = ''

    for char in fio:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я' or char == ' ':
            clean_fio += char
    
        

    return clean_fio

print(clean_name("Иsвtrан Ив^%ан Ива?но)вич)"))


"""
    Дан массив цен акций, вывести список, содержащий темпы прироста от периода к периоду.
    Для первого элемента списка выведите значение None. Округлите до целых.
    Например: [100, 150, 300, 400] -> [None, 50%, 100%, 33%]
"""


def get_pct_growth(s: list[float]) -> list[float]:

    start_price = s[0]
    profit = []

    for price in s:
        if price == start_price:
            profit.append(None)
            continue
        
        profit.append(f"{round((price / start_price - 1) * 100)}%")
        start_price = price

    return profit



