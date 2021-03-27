def isDifferent(a, b, c):
    if a == b and b == c and a == c:
        return False
    return True


def calculate(x_1, x_2, x_3, f_1, f_2, f_3):
    numerator = (x_2 - x_1) ** 2 * (f_2 - f_3) - (x_2 - x_3) ** 2 * (f_2 - f_1)
    denominator = (x_2 - x_1) * (f_2 - f_3) - (x_2 - x_3) * (f_2 - f_1)

    u = x_2 - numerator / (2 * denominator)

    return u  # point of min of our parabol


def run():
    # variables:
    y = lambda x: np.sin(x) - np.log(x * x) + 10 # our func

    a = 0  # left border
    c = 0  # right border

    x = 0  # min of func at now
    w = 0  # second low value of func
    v = 0  # last value of w
    u = 0  # min of approciate parabola
    epsilon = 0  # accuracy

    f_x = 0 # y(x)
    f_w = 0 # y(w)
    f_v = 0 # y(v)

    # init input:
    print("Left border: ")
    a = float(input())
    print("Right border: ")
    c = float(input())
    print("Accuracy: ")
    epsilon = float(input())

    # init values:
    k = (3 - sqrt(5)) / 2
    x = (a + c) / 2
    w = x
    v = x

    f_x = y(x)
    f_w = f_x
    f_v = f_x

    d = c - a # now step
    e = d # last step

    while True: # !!! поменять на условие сходимости g = e, e = d
        g = e

        if isDifferent(x, w, v) and isDifferent(f_x, f_w, f_v):
            u = calculate() # !!! понять что калькулировать
        
        if (a + epsilon) <= u and u <= (c - epsilon) and math.abs(u - x) < g/2:
            d = math.abs(u - x)
        else:
            if x < (c - a)/2:
                u = x + k * (c - x) # Golden ratio [x,c]
                d = c - x
            else:
                u = x - k * (x - a) # Golden ratio [a,x]
                d = x - a
            
            if math.abs(u - x) < epsilon:
                u = x + numpy.sign(u - x) * epsilon # minimal range between u and x

            f_u = y(u)
            if f_u <= f_x:
                if u >= x:
                    a = x
                else:
                    c = x

                v = w
                w = x
                x = u
                f_v = f_w
                f_w = f_x
                f_x = f_u
            else:
                if u >= x:
                    c = u
                else:
                    a = u
                
                if f_u <= f_w or w = x:
                    v = w
                    w = u
                    f_v = f_w
                    f_w = f_u
                elif f_u <= f_v or v = x or v = w:
                    v = u
                    f_v = f_u

    return x
