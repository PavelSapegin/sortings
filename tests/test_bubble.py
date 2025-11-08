import pytest
from sorts import bubblesort


@pytest.mark.parametrize(
        ["arr","expected"],
        [
            ([-10],[-10]),
            ([1,2,3,4,5],[1,2,3,4,5]),
            ([90,80,70,60,50,40],[40,50,60,70,80,90]),
            ([],[])
            ]
        )
def test_bubblesort_true(arr,expected):
    assert bubblesort(arr) == expected
