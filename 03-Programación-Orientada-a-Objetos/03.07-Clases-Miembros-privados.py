#####################################################################
# Clases - Miembros privados                                        #
#####################################################################

"""
 Las variables «privadas», que no pueden accederse excepto desde dentro de un objeto,
 no existen en Python. 

 Sin embargo, hay una convención que se sigue en la mayoría del código Python: un nombre 
 prefijado con un guión bajo (por ejemplo, _spam) debería tratarse como una parte no pública.

 Cualquier identificador con la forma __spam (al menos dos guiones bajos al principio,
 como mucho un guión bajo al final) es textualmente reemplazado por _nombredeclase__spam.
"""

class Demo:
    __Clave = "12345678a"

    def publico(self):
        print("Todos puede saber")

    def _privado(self):
        print("Nadie debería saber")

    def __secreto(self):
        print(f"Nadie puede saber el secreto: {self.__Clave}")

    def getSecreto(self, pw):
        if (pw == "1234"):
            self.__secreto()
        else:
            print("Sin acceso")


demo = Demo()

demo.publico()
demo._privado()
demo.getSecreto("1234")
print("")

print(dir(demo))
demo._Demo__secreto()
print(f"Clave: {demo._Demo__Clave}")