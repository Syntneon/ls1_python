from lesson_2 import  get_views_count, get_pairs_of_numbers, get_pct_growth, clean_name, move_zeros_2

def test_is_get_views_count():
  
    assert get_views_count(1) == "1 просмотр"
    assert get_views_count(2) == "2 просмотра"
    assert get_views_count(5) == "5 просмотров"
    assert get_views_count(11) == "11 просмотров"
    assert get_views_count(21) == "21 просмотр"
    assert get_views_count(23) == "23 просмотра"
    assert get_views_count(114) == "114 просмотров"


def test_get_pairs_with_sum():
    
    assert get_pairs_of_numbers([1, 2, 4, 3, 5, 2], 7) == [(4,3), (5,2)]
    assert get_pairs_of_numbers([1, 2, 4, 3, 5, 2, 1, 1], 2) == [(1, 1)]
    assert get_pairs_of_numbers([2, 4, 5, 8], 6) ==[(4, 2)]
    assert get_pairs_of_numbers([1, 7, 12], 7) == []
    assert get_pairs_of_numbers([1, 7, 12, 10, 8, 7, 5], 15) == [(8, 7), (10, 5)]

def test_get_pct_growth():

    assert get_pct_growth([50, 75, 112.5, 168.75]) == [None, '50%', '50%', '50%']
    assert get_pct_growth([200, 150, 100, 50]) == [None, '-25%', '-33%', '-50%']
    assert get_pct_growth([100, 100, 100, 100]) == [None, None, None, None]
    
def test_get_clean_name():

    assert clean_name("NbТим5офеев А2ндрей В88икторович") == "Тимофеев Андрей Викторович"
    assert clean_name("") == ""
    assert clean_name("!@#$%") == ""
    assert clean_name("Иsвtrан Ив^%ан Ива?но)вич)")

def test_get_move_zeros_2():
    
    assert move_zeros_2([1, 0, 0, 2, 3, 0, 1]) == [1, 2, 3, 1, 0, 0, 0]
    assert move_zeros_2([0, 0, 0]) == [0, 0, 0]
    assert move_zeros_2([1, 2, 3]) == [1, 2, 3]
    assert move_zeros_2([]) == []
    assert move_zeros_2([0, 1, 0, 2]) == [1, 2, 0, 0]
