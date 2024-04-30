from os import system

hucha = {"50": 0, "100": 0, "200": 0, "500": 0, "1000": 0}
total = 0

try:
    while (True):        
        accion = input("R para romper hucha, I para insertar monedas: ").upper()

        if (accion == "I"):
            while (True):
                moneda = input("Valor de la moneda (50, 100, 200, 500 o 1000): ")
                if (moneda in hucha.keys()):
                    system("cls")

                    hucha[moneda] += 1
                    total = 0

                    for key in hucha:
                        print(f"{hucha[key]} monedas de {key}")
                        total += int(key) * hucha[key]

                    print(f"\nImporte total: {total:1.2f}\n")

                    break
                else:
                    print(f"La moneda {moneda} no es de un valor valido.")
        elif(accion == "R"):
            system("cls")

            print(f"\nImporte total: {total:1.2f}\n")

            break
except Exception as err:
    print("No se puede mostrar información sobre la hucha.")
    print(err)
