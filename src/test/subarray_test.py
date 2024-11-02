import pytest

from subarrays.non_optimal import get_num_sub_arrays


def test_single_element():
    assert get_num_sub_arrays([1], 1) == 1

def test_both_elements():
    assert get_num_sub_arrays([2, 2], 2) == 2


def test_all_combination_of_3():
    assert get_num_sub_arrays([1, 2, 3], 6) == 6

def test_long_array():
    long_arr = list(range(1, 10))
    assert get_num_sub_arrays(long_arr, 6) == 9

@pytest.mark.timeout(3)
def test_efficient_very_long_array():
    long_arr = list(range(1, 1_000_000))
    assert get_num_sub_arrays(long_arr, 6) == 9
