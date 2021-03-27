import numpy as np

def run():
    print("Left border: ")
    left_border = int(input())
    print("Right border: ")
    right_border = int(input())
    print("ε:")
    e = float(input())
    golden_ratio_value_1 = (3 - np.sqrt(5)) / 2
    golden_ratio_value_2 = 1 - golden_ratio_value_1
    y = lambda x: np.sin(x) - np.log(x * x) + 10
    x_1 = golden_ratio_value_1 * (right_border - left_border) + left_border
    x_2 = golden_ratio_value_2 * (right_border - left_border) + left_border

    x_1_value = y(x_1)
    x_2_value = y(x_2)

    iter_amount = 0
    while (right_border - left_border) / 2 > e:
        if x_1_value > x_2_value:
            left_border = x_1
            x_1 = x_2
            x_1_value = x_2_value
            x_2 = golden_ratio_value_2 * (right_border - left_border) + left_border
            x_2_value = y(x_2)
        elif x_1_value < x_2_value:
            right_border = x_2
            x_2 = x_1
            x_2_value = x_1_value
            x_1 = golden_ratio_value_1 * (right_border - left_border) + left_border
            x_1_value = y(x_1)
        else:
            left_border = x_1
            right_border = x_2
            x_1 = golden_ratio_value_1 * (right_border - left_border) + left_border
            x_2 = golden_ratio_value_2 * (right_border - left_border) + left_border
            x_1_value = y(x_1)
            x_2_value = y(x_2)
        iter_amount += 1
        print(f"Left border: {left_border}")
        print(f"Right border: {right_border}")
        print()
    minimum = (left_border + right_border) / 2
    print(f"Iter amount: {iter_amount}")
    print(f"Minimum: {minimum}")
    print(f"Minimum value: {y(minimum)}")
    print("Уменьшается на константу золотого сечения")

