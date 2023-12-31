def compound(sum, annual_return, annual_cost, time_periods):
    for _ in range(time_periods):
        sum *= (1 + annual_return) * (1 - annual_cost)

    return sum
