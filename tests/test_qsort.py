import pytest
from sorts import qsort


@pytest.mark.parametrize(
    ["arr","expected"],
    [
        ([],[]),
        ([5,4,3,2,1],[1,2,3,4,5]),
        ([9,9,9,9],[9,9,9,9]),
    ]
)
def test_qsort_true(arr,expected):
    assert qsort(arr) == expected
