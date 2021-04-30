import gradient_method as gm
import newton_ofigel_i_nachal_flexit as newt

fun = lambda x: 2 * x ** 2 + 3 * x + 3
der_fun = lambda x: 4 * x + 3

gm.gradient_method(fun, der_fun, 0.1, 40)
newt.newton(fun, der_fun, 0.1)
