from Methods import Parabola, Dichotomy, GoldenRatio, Fibonacci, Brent

print("---Algorithm---")
print("1. Dichotomy")
print("2. GoldenRatio")
print("3. Fibonacci")
print("4. Parabola")
print("5. Brent")
print("---------------")

var = int(input("-> "))

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