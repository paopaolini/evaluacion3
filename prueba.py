#Esta es una evaluación que corresponde a una Ejecución Práctica. 

#La evaluación consiste en: 
#Construir soluciones de algoritmos de acuerdo con las instrucciones necesarias que den solución al requerimiento del cliente
#Contexto y requerimiento:
#Sistema de Gestión de Habitaciones de Hotel
#Descripción:
#Crear un programa que simule la gestión de habitaciones en un hotel. El hotel tiene 5 pisos y cada piso tiene 8 habitaciones. El programa debe permitir ver el estado de las habitaciones, reservar una habitación específica, anular una reserva y totalizar el número de habitaciones reservadas. Las habitaciones del piso 5 son premium y tienen un costo de 100.000 pesos diarios. Las habitaciones del piso 4 cuestan $60.000 y el resto de las habitaciones cuestan $30.000.
#En este registro, se requiere construir un programa con un menú que contenga las siguientes opciones:

#La información de cada habitación se compone de los datos: Número de habitación, estado de reserva, valor diario de la reserva, nombre, apellido, rut, fecha:hora de entrada y fecha:hora de salida.


#Opción 1 
#Reservar: se ejecuta la función reservar_habitacion. Para esto se debe pedir el nombre, apellido y rut de la persona responsable, la fecha y hora de ingreso y la fecha y hora de salida. Solo se reserva una habitación si se paga inmediatamente, por lo que se entiende que no hay habitaciones reservadas sin ocupar.
#Debe verificar que todos los datos ingresados sean válidos. (try/except)

#Opción 2 
#Buscar: se ejecuta la función buscar_habitacion: Corresponde buscar una habitación por su código, el cual se debe pedir al usuario, ser enviado a la función y como resultado mostrar toda su información almacenada. El código de cada habitación se compone por su piso y número, por ejemplo, las habitaciones 13, 34, 58, corresponden a la habitación 3 del primero piso, cuarta habitación del 4to piso y octava habitación del piso 5 respectivamente.

#Opción 3 
#Estado: se ejecuta la función ver_estado de las habitaciones: Esta opción, permite la impresión por pantalla de todas las habitaciones independiente del estado (disponibles o reservadas). Muestra toda la información de cada una de las habitaciones.

#Opción 4
#Ventas: se ejecuta la función ventas_diarias: Esta función calcula el total de las ventas del día sumando todas las habitaciones que están reservadas dentro del día que se entrega a la función y lo muestra por pantalla
#Opción 5 
#Guardar la información: Se ejecuta la función guardar la cual guarda en un archivo.csv todo el estado de todas las habitaciones según la estructura de los datos definida al comienzo de este ejercicio.
#Opción 6
#Salir. Corresponde a salir del programa emitiendo un mensaje de salida.




import csv 

print("Bienvenido al Hotel Habitaciones ")
print(" ________________________________ ")
print("|           Menu.                |")
print("|________________________________|")
print("|1.Reservar habitacion.          |") 
print("|2.Buscar habitacion.            |")
print("|3.Ver habitaciones disponible.  |")
print("|4.Ver total de ventas.          |")
print("|5.Guardar datos.                |")
print("|________________________________|")
seleccion_menu=int(input("       Seleccione opciones:"))
if seleccion_menu==1:
    nombre=input("ingrese nombre: ")
    Runt=int(input("ingrese RUT: "))
    hora_ingreso=int(input("ingrese hora de ingreso: "))
    fecha_ingreso=int(input("fecha de ingreso: "))
    hora_salida=int(input("ingrese horade salida: "))

elif seleccion_menu==2:
    habitacion_buscar=int(input("ingrese habitacion que desea buscar"))

elif seleccion_menu==3:
    print("INFORMACION DE HABITACIONES DISPONIBLES")
    print("NO ESTA  DISPONIBLE ")

elif seleccion_menu==4:
    print("TIENE 1.000.000.000 RECAUDADO")

elif seleccion_menu==5:
    print("SE HA GUARDADO BN")
