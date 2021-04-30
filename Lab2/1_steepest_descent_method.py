import math
import numpy as np

def brent(y, e):
    a = 0 # left border
    b = 1000 # right border
    accuracy = e

    K = (3 - math.sqrt(5)) / 2
    x = (a + b) / 2
    w = x
    v = x

    f_x = y(x)
    f_w = f_x
    f_v = f_x

    d = b - a
    e = d

    while b - a >= accuracy:
        g = e
        e = d
        parabola_fit = False

        if abs(x - (a + b) / 2) + (b - a) / 2 <= 2 * accuracy:
            break

        if (x != w) and (x != v) and (w != v) and (f_x != f_w) and (f_x != f_v) and (f_w != f_v):
            f_val = dict()
            f_val[x] = f_x
            f_val[w] = f_w
            f_val[v] = f_v

            l = sorted([x, w, v])[0]
            m = sorted([x, w, v])[1]
            r = sorted([x, w, v])[2]

            f_1, f_2, f_3 = f_val[l], f_val[m], f_val[r]

            u = m - ((m - l) ** 2 * (f_2 - f_3) - (m - r) ** 2 * (f_2 - f_1)) / (
                        2 * ((m - l) * (f_2 - f_3) - (m - r) * (f_2 - f_1)))

            if u >= a + accuracy and u <= b - accuracy and abs(u - x) < g / 2:
                d = abs(u - x)
                parabola_fit = True

                if (u - a < 2 * accuracy) or (b - u) < 2 * accuracy:
                    u = x - np.sign(x - (a + b) / 2) * accuracy

        if not parabola_fit:
            if x < (b + a) / 2:
                u = x + K * (b - x)
                d = b - x
            else:
                u = x - K * (x - a)
                d = x - a
            if abs(u - x) < accuracy:
                u = x + np.sign(u - x) * accuracy

        f_u = y(u)
        d = abs(u - x)

        if f_u <= f_x:
            if u >= x:
                a = x
            else:
                b = x
            v = w
            w = x
            x = u
            f_v = f_w
            f_w = f_x
            f_x = f_u
        else:
            if u >= x:
                b = u
            else:
                a = u
            if f_u <= f_w or w == x:
                v = w
                w = u
                f_v = f_w
                f_w = f_u
            elif f_u <= f_v or v == x or v == w:
                v = u
                f_v = f_u

    return (a+b)/2

def searchLambda(x, antigrad, e):
    y = lambda l: x - l * antigrad(x)
    return brent(y, e)

def run(function, antigrad):
    print("Enter a start point:")
    now = float(input())

    print("Enter a accuracy:")
    e = float(input())

    last = now + 2 * e

    while abs(last - now) > e:
        l = searchLambda(now, antigrad, e)
        temp = now
        now = now - l * antigrad(now)
        last = temp
    
    return now