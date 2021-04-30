def newton(fun, der_fun, e):
    x = 1
    prev_x = 100
    while abs(x - prev_x) >= e:
        prev_x = x
        if der_fun(prev_x) == 0:
            print(f'x: {prev_x}, y: {fun(prev_x)}')
            return
        x = prev_x - fun(prev_x) / der_fun(prev_x)
    print(f'x: {x}, y: {fun(x)}')
