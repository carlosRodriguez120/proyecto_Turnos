# decorador____________________________________________________________________________________________________________
def decorador(num):
    print("_" * 25)
    print(f"su numero es: ")
    if num == 1:
        print(next(c))
    elif num == 2:
        print(next(d))
    elif num == 3:
        print(next(p))
    print("aguarde y sera atendido")
    print("_" * 25)


# ______________________________________________________________________________________________________________________

def turnoCosmetica():
    for num in range(1, 10000000000):
        yield f"C-{num}".center(10, " ")


def turnoDrogueria():
    for num in range(1, 10000000000):
        yield f"D-{num}".center(10, " ")


def turnoPerfumeria():
    for num in range(1, 10000000000):
        yield f"P-{num}".center(10, " ")


c = turnoCosmetica()
d = turnoDrogueria()
p = turnoPerfumeria()
