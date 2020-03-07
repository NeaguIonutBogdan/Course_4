from numpy import log as np
import math
x = int(input("introduceti un nr intreg:"))#3
def calcul(x):
    if isinstance(x, int):
        return x
    else:
        print("Intrroduceti un numar intreg!")
def A(x):
    print(abs(x) * x ** 3)
def B(x):
    if x >= 0:
        print(math.log10(x) + math.log(x))
    else:
        print("Trebuia sa intrroduceti un numar intreg pozitiv!")
def C(x):
    print(math.sin(x) + (math.sin(x) * math.cos(x)))
def D(x):
    e = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274
    print(e**x + 2 * math.atan(x)-x)
calcul(x)
print("x: ", end = '')
print(x)
print("def A: ", end = '')
A(x)
print("def B: ", end = '')
B(x)
print("def C: ", end = '')
C(x)
print("def D: ", end = '')
D(x)