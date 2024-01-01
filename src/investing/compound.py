def compound(sum, annual_return, annual_cost, years):
    # for _ in range(years):
    #     sum *= (1 + annual_return) * (1 - annual_cost)
    result = (
        sum * (1 + annual_return - annual_cost - (annual_return * annual_cost)) ** years
    )

    return result


if __name__ == "__main__":
    while True:
        input_str = input("Enter: start_sum  annual_return  annual_cost  years\n>")
        input_list = input_str.split()
        try:
            result = compound(
                float(input_list[0]),
                float(input_list[1]),
                float(input_list[2]),
                int(input_list[3]),
            )
            print("\nThe value is: " + str(result) + "\n")

        except Exception as e:
            print("\n" + str(e) + "\n")
