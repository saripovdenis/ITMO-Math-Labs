import Methods/Dichotomy
import Methods/Parabola
import Methods/GoldenRatio
import Methods/Fibonacci
print("---Algorithm---")
pritn("1. Dichotomy")
pritn("2. GoldenRatio")
pritn("3. Fibonacci")
pritn("4. Parabola")
pritn("5. Brent (not implemented)")
print("---------------")
print("-> ")

var = int(input())

if var == 1:
    Dichotomy.run()
elif var == 2:
    GoldenRatio.run()
elif var == 3:
    Fibonacci.run()
elif var == 4:
    Parabola.run()
else:
    print("Unknown algo")