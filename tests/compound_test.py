import pytest

from src.investing.compound import compound


@pytest.mark.parametrize(
    "start_sum,annual_return,annual_cost,annual_installment,years,expected",
    [
        (100000, 0.2473, 0.002, 0, 1, 124480.54000000002),
        (
            100000,
            0.2473,
            0.002,
            0,
            3,
            192887.6361838944,  # what the value is after 3 years.
        ),
    ],
)
def test_compound(
    start_sum, annual_return, annual_cost, annual_installment, years, expected
):
    actual = compound(start_sum, annual_return, annual_cost, annual_installment, years)
    assert actual == expected


@pytest.mark.parametrize(
    "start_sum,annual_return,annual_cost,annual_installment,years,expected",
    [
        (
            100000,
            0.16,
            0.0022,
            5000,
            1,
            115744.8,  # no installment added, not even the initial value
        ),
        (100000, 0.16, 0.0022, 5000, 2, 139755.82727039998),
        (
            100000,
            0.16,
            0.0022,
            5000,
            5,
            236946.4774714958,
        ),
    ],
)
def test_compound_with_annual_installments(
    start_sum, annual_return, annual_cost, annual_installment, years, expected
):
    actual = compound(start_sum, annual_return, annual_cost, annual_installment, years)
    assert actual == expected
