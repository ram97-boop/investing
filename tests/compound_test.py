from src.investing.compound import compound


def test_compound():
    start_sum = 100000
    annual_return = 0.2473
    annual_cost = 0.002
    time_periods = 1

    expected = 124480.54000000002
    actual = compound(start_sum, annual_return, annual_cost, time_periods)
    assert actual == expected
