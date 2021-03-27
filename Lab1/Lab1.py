import Methods/Dichotomy
import Methods/Parabola
import Methods/GoldenRatio
import Methods/Fibonacci
import Methods/Brent
print("---Algorithm---")
pritn("1. Dichotomy")
pritn("2. GoldenRatio")
pritn("3. Fibonacci")
pritn("4. Parabola")
pritn("5. Brent")
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
elif var == 5:
    Brent.run()
else:
    print("Unknown algo")