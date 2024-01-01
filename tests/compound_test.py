import pytest

from src.investing.compound import compound


@pytest.mark.parametrize(
    "start_sum,annual_return,annual_cost,years,expected",
    [
        (100000, 0.2473, 0.002, 1, 124480.54000000002),
        (
            100000,
            0.2473,
            0.002,
            3,
            192887.6361838944,  # what the value is after 3 years.
        ),
    ],
)
def test_compound(start_sum, annual_return, annual_cost, years, expected):
    actual = compound(start_sum, annual_return, annual_cost, years)
    assert actual == expected
