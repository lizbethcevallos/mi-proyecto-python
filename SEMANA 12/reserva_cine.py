# Programa: Reserva de un asiento en una sala de cine

# Crear una matriz de 3 filas por 4 columnas
# 0 = asiento libre
# 1 = asiento reservado
asientos = [
    [0, 0, 0, 0,],
    [0, 0, 0, 0,],
    [0, 0, 0, 0,]
]

# Solicitar al usuario la fila y columna del asiento 
fila = int (input("Ingrese la fila del asiento (0 a 2): "))
columna = int (input("Ingrese la columna del asiento (0 a 3): "))

# Reservar el asiento seleccionado
asientos[fila][columna] = 1

# Mostrar el estado completo de la sala
print("\nEstado de la sala:")

for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()