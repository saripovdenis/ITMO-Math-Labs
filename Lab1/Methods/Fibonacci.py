import numpy as np
def run():
    print("Left border: ")
    left_border = int(input())
    print("Right border: ")
    right_border = int(input())
    print("ε:")
    e = float(input())
    n = 1

    y = lambda x: np.sin(x) - np.log(x * x) + 10
    fib = lambda m: 1 / np.sqrt(5) * (((1 + np.sqrt(5)) / 2) ** m - ((1 - np.sqrt(5)) / 2) ** m)
    while fib(n) <= (right_border - left_border) / e:
        n += 1

    x_1 = left_border + fib(n - 2) / fib(n) * (right_border - left_border)
    x_2 = left_border + fib(n - 1) / fib(n) * (right_border - left_border)

    x_1_value = y(x_1)
    x_2_value = y(x_2)

    prev_x_1 = 0
    for i in range(1, n - 1):
        prev_x_1 = x_1
        if x_1_value > x_2_value:
            left_border = x_1
            x_1 = x_2
            x_2 = left_border + fib(n - i - 1) / fib(n - i) * (right_border - left_border)
            x_1_value = x_2_value
            x_2_value = y(x_2)
        else:
            right_border = x_2
            x_2 = x_1
            x_1 = left_border + fib(n - i - 1) / fib(n - i) * (right_border - left_border)
            x_2_value = x_1_value
            x_1_value = y(x_1)
    minimum = (left_border + right_border) / 2
    print(f"Iter amount: {n}")
    print(f"Minimum: {minimum}")
    print(f"Minimum value: {y(minimum)}")

