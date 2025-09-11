def two_lists_to_dict(keys: list[str], income: list[int]) -> dict:
    """
        Соединить два списка в словарь
    """
    
    return {keys[i]: income[i] for i in range(len(keys))}


keys = ["USA", "Russia", "France"]
income = [100, 10, 25]

# print(two_lists_to_dict(keys, income))




def merge_two_dicts(dict_1: dict, dict_2: dict) -> dict:
    """
        Соединить два словаря
    """
  
    return dict_1 | dict_2

  
developed_markets = {
        "USA": 100,
        "Japan": 90,
        "France": 25
    }

emerging_markets = {
        "China": 80,
        "India": 50,
        "Russia": 5
    }

# print(merge_two_dicts(developed_markets, emerging_markets))

def sort_dict_values(your_dict: dict) -> dict:
    """
        Отсортировать словарь по убыванию
    """

    return dict(sorted(your_dict.items(), key=lambda item: item[1], reverse=True))

d = {
        "USA": 100,
        "Japan": 90,
        "France": 25,
        "China": 80,
        "India": 50,
        "Russia": 5
    }
print(sort_dict_values(d))

   

def value_of_the_same_key_kinds(monthly_sales: dict) -> dict:
    """
        Просуммировать словарь по годам
    """
    
    value_years_dict = {}
    currency_year = ''

    for key, value in monthly_sales.items():

        currency_year = key.split('_')[1]

        if currency_year in value_years_dict:
            value_years_dict[currency_year] += value
        else:
            value_years_dict[currency_year] = value

    return value_years_dict
       


monthly_sales = {
        "Jan_2020": 100,
        "Feb_2020": 90,
        "Mar_2020": 15,
        "Jan_2021": 10,
        "Feb_2021": 50,
        "Mar_2022": 5,
        "Sep_2023": 12,
        "Oct_2023": 12
    }

# print(value_of_the_same_key_kinds(monthly_sales))

def fill_dict(yearly_sales: dict) -> dict:

    """
    Создает словарь со всеми годами (ключи)
    """
    years = list(yearly_sales.keys())
    start_year = int(years[0])
    end_year = int(years[-1])
    all_yearly_sales = {}

    for year in range(start_year, end_year + 1):

        key = str(year)
        all_yearly_sales[key] = yearly_sales.get(key, 0)

    return all_yearly_sales





def fill_missed_years(yearly_sales: dict) -> dict:
    
    """
        Заполнить пропущенные значения средним арифметическим двух соседних значений.
        Например, если в 2015 году значение равно 50, в 2018 - 80, 
        то в 2016 должно быть 60, в 2017 - 70
    """

    target = fill_dict(yearly_sales)
    first_value = None
    missing_years = []
    step_index = 1

    for year, value in target.items():
        if value != 0:
            if missing_years:
                step = (value - first_value) / (1 + len(missing_years))
                for y in missing_years:
                    target[y] = round(first_value + step * step_index)
                    step_index += 1 
                missing_years = []
                step_index = 1
            first_value = value
            
        else:
            missing_years.append(year)
    return target


yearly_sales = {
        "2015": 50,
        "2018": 65,
        "2019": 120,
        "2023": 160,
        "2025": 200
    }
# print(fill_missed_years(yearly_sales))




_sales_data = [
    {
        "category": "dairy products",
        "product": "milk",
        "price_rub": 100,
        "count": 1
    },
    {
        "category": "dairy products",
        "product": "cream",
        "price_rub": 290,
        "count": 1
    },
    {
        "category": "dairy products",
        "product": "yogurt",
        "price_rub": 50,
        "count": 1
    },
    {
        "category": "bakery",
        "product": "white_bread",
        "price_rub": 60,
        "count": 1
    },
    {
        "category": "bakery",
        "product": "black_bread",
        "price_rub": 55,
        "count": 1
    },
    {
        "category": "drinks",
        "product": "water",
        "price_rub": 90,
        "count": 1
    },
    {
        "category": "drinks",
        "product": "apple_juice",
        "price_rub": 300,
        "count": 1
    }
]


def get_distinct_categories(sales_data: list) -> set:

    """
        Вернуть множество уникальных категорий товаров
        Воспользоваться set comprehension (по аналогии с list/dict comprehension)
    """
   
    return {category['category'] for category in sales_data}

# print(get_distinct_categories(_sales_data))


def sum_category_as_tuples(sales_data: list) -> list:
    """
        Показать сумму покупок по категориями. Отсортировать категории по возрастанию суммы
    """
    category_and_price = {}

    for item in sales_data:
        cat = item['category']
        price = item['price_rub']
        category_and_price[cat] = category_and_price.get(cat, 0) + price
    
    result = sorted(category_and_price.items(), key= lambda x: x[1])
    return result


   
# print(sum_category_as_tuples(_sales_data))

