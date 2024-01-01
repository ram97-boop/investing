def compound(sum, annual_return, annual_cost, annual_installment, years):
    rate = 1 + annual_return - annual_cost - annual_return * annual_cost

    result = sum * (rate**years)

    annual_installment_result = 0
    for y in range(1, years):
        annual_installment_result += annual_installment * (rate**y)

    return result + annual_installment_result


if __name__ == "__main__":
    while True:
        input_str = input(
            "Enter: start_sum  annual_return  annual_cost  annual_installment  years\n>"
        )
        input_list = input_str.split()
        try:
            result = compound(
                float(input_list[0]),
                float(input_list[1]),
                float(input_list[2]),
                float(input_list[3]),
                int(input_list[4]),
            )
            print("\nThe value is: " + str(result) + "\n")

        except Exception as e:
            print("\n" + str(e) + "\n")
