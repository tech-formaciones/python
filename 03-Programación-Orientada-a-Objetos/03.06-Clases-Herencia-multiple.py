#####################################################################
# Clases - Herencia multiple                                        #
#####################################################################

# Definición de la clase A
class A:
    Numero1 = None
    Numero2 = None

    def __init__(self) -> None:
        print("constructor A")

    def Suma(self) -> int:
        return f"A >> {str(self.Numero1 + self.Numero2)}"
    
    def Resta(self) -> int:
        return f"A >> {str(self.Numero1 - self.Numero2)}"

# Definición de la clase B
class B:
    Numero1 = None
    Numero2 = None

    def __init__(self, n1, n2) -> None:
        self.Numero1 = n1
        self.Numero2 = n2
        print("constructor B")

    def Suma(self) -> int:
        return f"B >> {str(self.Numero1 + self.Numero2)}"

    def Multiplica(self) -> int:
        return f"B >> {str(self.Numero1 * self.Numero2)}"


# Definimos la clase CALCULADORA que hereda de A y B
# Cuando el nombre de las funciones coincide solo se hereda la función de la clase
# más a la izquierda (la espeficada en primer lugar)
class Calculadora(A, B): pass

c = Calculadora()
c.Numero1 = 10
c.Numero2 = 15
print(f"Numero 1: {c.Numero1}")
print(f"Numero 2: {c.Numero2}")
print(f"Suma: {c.
Suma()}")
print(f"Resta: {c.Resta()}")
print(f"Multiplica: {c.Multiplica()}")