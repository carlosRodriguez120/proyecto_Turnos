import numeros


def inicio():
    num = "x"
    while not num.isnumeric() or int(num) not in range(1, 5):
        print("Elige una opcion:")
        print('''
           [1] - cosmetica
           [2] - drogueria
           [3] - perfumeria
           [4] - salir''')
        try:
            num = input()
            [1,2,3,4].index(num)
        except ValueError:
            print("elija un valor correcto ")

    return int(num)


finalizar_programa = False

while not finalizar_programa:
    menu = inicio()
    numeros.decorador(menu)

