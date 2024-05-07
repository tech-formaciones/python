#####################################################################
# Clases - Miembros privados                                        #
#####################################################################

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