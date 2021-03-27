import numpy as np

def run():
    print("Left border: ")
    left_border = int(input())
    print("Right border: ")
    right_border = int(input())
    print("ε:")
    e = float(input())

    y = lambda x: np.sin(x) - np.log(x * x) + 10
    middle = (left_border + right_border) / 2
    delta = e / 2
    x_1 = left_border
    x_2 = right_border
    predicted_iter_amount = np.log((right_border - left_border) / e) / np.log(2)
    iter_amount = 0
    while (right_border - left_border) / 2 > e:
        iter_amount += 1
        x_1 = middle - delta
        x_2 = middle + delta
        x_1_value = y(x_1)
        x_2_value = y(x_2)
        if x_1_value > x_2_value:
            left_border = x_1
        elif x_1_value < x_2_value:
            right_border = x_2
        else:
            left_border = x_1
            right_border = x_2
        middle = (left_border + right_border) / 2
        delta = e / 2

    minimum = middle
    print(f"Predicted iter amount: {predicted_iter_amount}")
    print(f"Iter amount: {iter_amount}")
    print(f"Minimum: {minimum}")
    print(f"Minimum value: {y(minimum)}")
    print("Отрезок линейно уменьшается")