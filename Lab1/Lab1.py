import Methods/Dichotomy
import Methods/Parabola

print("---Algorithm---")
pritn("1. Dichotomy")
pritn("2. GoldenRatio (not implemented)")
pritn("3. Fibonacci (not implemented)")
pritn("4. Parabola (not implemented)")
pritn("5. Brent (not implemented)")
print("---------------")
print("-> ")

var = int(input())

if var == 1:
    Dichotomy.run
elif var == 4:
    Parabola.run
else:
    print("Unknown algo")