import numpy as np


def print_params(a, b, c):
    print("Left border: ", a, end=", ")
    print("Middle point: ", b, end=", ")
    print("Right border: ", c, end=".\n")


def condition(y, a, b, c):
    if y(b) < y(a) and y(b) < y(c):
        return True
    return False


def calculate(y, x_1, x_2, x_3):
    f_1 = y(x_1)
    f_2 = y(x_2)
    f_3 = y(x_3)

    numerator = (x_2 - x_1) ** 2 * (f_2 - f_3) - (x_2 - x_3) ** 2 * (f_2 - f_1)
    denominator = (x_2 - x_1) * (f_2 - f_3) - (x_2 - x_3) * (f_2 - f_1)
    u = x_2 - numerator / (2 * denominator)

    return u  # point of min of our parabol


def run():
    print("Left border: ")
    left_border = int(input())  # 2
    print("Right border: ")
    right_border = int(input())  # 7
    print("Middle point:")
    middle_point = float(input())  # 4
    print("ε:")
    accuracy = float(input())  # 0.000001

    y = lambda x: np.sin(x) - np.log(x * x) + 10

    min = 0  # y(min) - smallest on the segment
    iteration = 0 # count iterations

    # check input values
    while condition(y, left_border, middle_point, right_border) == False:
        print("Choose any other middle point, which satisfies the condition: f1 > f2 < f3")
        middle_point = float(input())

    flag = True
    while flag:
        iteration += 1
        print_params(left_border, middle_point, right_border)

        if (right_border - left_border) <= accuracy or (right_border - middle_point) <= accuracy or (middle_point - left_border) <= accuracy:
            print("accuracy stop")
            flag = False

        x_1 = left_border
        x_2 = middle_point
        x_3 = right_border

        u = calculate(y, x_1, x_2, x_3)

        min = u

        if u == x_1 or u == x_2 or u == x_3:
            print("without accuracy")
            flag = False

        # reset borders
        if x_1 < u and u < x_2 and condition(y, x_1, u, x_2):
            left_border = x_1
            middle_point = u
            right_border = x_2
        elif x_2 < u and u < x_3 and condition(y, x_2, u, x_3):
            left_border = x_2
            middle_point = u
            right_border = x_3
        elif x_1 < u and u < x_3 and condition(y, x_1, u, x_3):
            left_border = x_1
            middle_point = u
            right_border = x_3
        else:
            print("Something went wrong.")
            print_params(left_border, middle_point, right_border)
            flag = False

    print(f"Min(x): x = {min}, Min(y): y = {y(min)}")
    print(f"Number of iterations - {iteration}")
    return min
