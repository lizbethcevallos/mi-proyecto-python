# Programa: Agenda de contactos
# Uso de diccionarios en Python

# Diccionario para almacenar contactos
contactos = {
    "Ana": "0991234567",
    "Carlos": "0987654321",
    "Maria": "0974567890"
}

# Mostrar contactos registrados
print("AGENDA DE CONTACTOS")
print("-------------------")

for nombre, telefono in contactos.items():
    print(nombre, ":", telefono)

# Agregar un nuevo contacto
print("\nAGREGAR CONTACTO")

nombre_nuevo = input("Ingrese el nombre: ")
telefono_nuevo = input("Ingrese el numero telefonico: ")

contactos[nombre_nuevo] = telefono_nuevo

print("Contacto agregado correctamente.")

# Mostrar contactos actualizados
print("\nCONTACTOS REGISTRADOS")

for nombre, telefono in contactos.items():
    print(nombre, ":", telefono)

# Buscar un contacto
buscar = input("\nIngrese el nombre del contacto que desea buscar: ")

if buscar in contactos:
    print("Numero telefonico:", contactos[buscar])
else:
    print("El contacto no se encuentra registrado.")

# Eliminar un contacto
eliminar = input("\nIngrese el nombre del contacto que desea eliminar: ")

if eliminar in contactos:
    del contactos[eliminar]
    print("Contacto eliminado correctamente.")
else:
    print("El contacto no existe.")

# Mostrar agenda final
print("\nAGENDA FINAL")

for nombre, telefono in contactos.items():
    print(nombre, ":", telefono)
    