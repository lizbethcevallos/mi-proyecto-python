# Semana 12 - Reserva de un asiento en sala de cine

# Estudiante
Estefania Lizbeth Cevallos Muñoz

# Objetivo

Desarrollar un programa en Python que permita gestionar la reserva de un asiento en una sala de cine utilizando una matriz de 3 filas por 4 columnas.

El programa solicita al usuario la fila y la columna del asiento que desea reservar, modifica la posición correspondiente de la matriz y muestra el estado completo de la sala utilizando bucles anidados.

# Funcionamiento

Los asientos se representan mediante los siguientes valores:

- 0 = Asiento libre
- 1 = Asiento reservado

El usuario debe ingresar:

- Una fila entre 0 y 2.
- Una columna entre 0 y 3.

El programa registra la reserva asignando el valor 1 al asiento seleccionado y posteriormente muestra la matriz completa de la sala.

# Ejemplo de ejecución

```text
Ingrese la fila del asiento (0 a 2): 1
Ingrese la columna del asiento (0 a 3): 2

Estado de la sala:
0 0 0 0
0 0 1 0
0 0 0 0
