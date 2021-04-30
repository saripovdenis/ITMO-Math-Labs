def gradient_method(fun, der_fun, step, iter_amount):
    prev_x = 0
    for i in range(iter_amount):
        temp_x = prev_x - step * der_fun(prev_x)
        prev_x = temp_x
    print(f'x: {temp_x}, y: {fun(temp_x)}')
