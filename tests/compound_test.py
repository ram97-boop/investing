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
            193661.51078,  # what the value is after 3 years.
        ),
    ],
)
def test_compound(start_sum, annual_return, annual_cost, years, expected):
    start_sum = 100000
    annual_return = 0.2473
    annual_cost = 0.002
    years = 1

    expected = 124480.54000000002
    actual = compound(start_sum, annual_return, annual_cost, years)
    assert actual == expected
