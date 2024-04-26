# Operadores Aritméticos
### **Un operador aritmético toma dos operandos (variables o valores) como entrada, realiza un cálculo y devuelve el resultado.**
&nbsp;
| Operador | Descripción                                        | Uso            |
| -------- | -------------------------------------------------- | -------------- |
| +        | Realiza Adición entre los operandos                | 12 + 3 = 15    |
| -        | Realiza Substracción entre los operandos           | 12 - 3 = 9     |
| *        | Realiza Multiplicación entre los operandos         | 12 * 3 = 36    |
| /        | Realiza División entre los operandos               | 12 / 3 = 4     |
| %        | Realiza un módulo entre los operandos              | 16 % 3 = 1     |
| **       | Realiza la potencia de los operandos               | 12 ** 3 = 1728 |
| //       | Realiza la división con resultado de número entero | 18 // 5 = 3    |

&nbsp;
&nbsp;
&nbsp;
# Operadores de Asignación
### ***Se utiliza un operador de asignación para asignar valores a una variable.***
### ***Esto generalmente se combina con otros operadores (como aritmética, bit a bit) donde la operación se realiza en los operandos y el resultado se asigna al operando izquierdo.***
&nbsp;
| Operador | Descripción                                   |
| -------- | --------------------------------------------- |
| =        | a = 5. El valor 5 es asignado a la variable a |
| +=       | a += 5 es equivalente a a = a + 5             |
| -=       | a -= 5 es equivalente a a = a - 5             |
| *=       | a *= 3 es equivalente a a = a * 3             |
| /=       | a /= 3 es equivalente a a = a / 3             |
| %=       | a %= 3 es equivalente a a = a % 3             |
| **=      | a **= 3 es equivalente a a = a ** 3           |
| //=      | a //= 3 es equivalente a a = a // 3           |

&nbsp;
&nbsp;
&nbsp;
# Operadores Relacionales
### ***Un operador relacional se emplea para comparar y establecer la relación entre ellos. Devuelve un valor booleano (true o false) basado en la condición.***
&nbsp;
| Operador | Descripción                                                                                 | Uso                    |
| -------- | ------------------------------------------------------------------------------------------- | ---------------------- |
| >        | Devuelve True si el operador de la izquierda es mayor que el operador de la derecha         | 12 > 3 devuelve True   |
| <        | Devuelve True si el operador de la derecha es mayor que el operador de la izquierda         | 12 < 3 devuelve False  |
| ==       | Devuelve True si ambos operandos son iguales                                                | 12 == 3 devuelve False |
| >=       | Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha | 12 >= 3 devuelve True  |
| <=       | Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda | 12 <= 3 devuelve False |
| !=       | Devuelve True si ambos operandos no son iguales                                             | 12 != 3 devuelve True  |

&nbsp;
&nbsp;
&nbsp;
# Operadores de Pertenencia
### ***Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).***
&nbsp;
- ***in*** devuelve *True* si el valor especificado se encuentra en la secuencia. En caso contrario devuelve *False*.

- ***not in*** devuelve *True* si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve *False*.

&nbsp;
&nbsp;
&nbsp;
# Operadores de Identidad
### ***Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.***
&nbsp;
- ***is*** devuelve *True* si los operandos se refieren al mismo objeto. En caso contrario devuelve *False*.

- ***is not*** devuelve*True* si los operandos no se refieren al mismo objeto. En caso contrario devuelve *False*.

Ten en cuenta que dos valores, cuando son iguales, no implica necesariamente que sean idénticos.

&nbsp;
&nbsp;
&nbsp;
# Operadores Lógicos
### ***Se utiliza un operador lógico para tomar una decisión basada en múltiples condiciones. Los operadores lógicos utilizados en Python son and, or y not.***
&nbsp;
| Operador | Descripción                                      | Uso     |
| -------- | ------------------------------------------------ | ------- |
| and      | Devuelve True si ambos operandos son True        | a and b |
| or       | Devuelve True si alguno de los operandos es True | a or b  |
| not      | Devuelve True si alguno de los operandos False   | not a   |