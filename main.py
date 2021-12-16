from tkinter import *
from abonados import Abonado
from telefono import *
import random


CAPACIDAD = 20
PORC_FUERA_DE_SERVICIO = 0.15
PORC_OCUPADO = 0.25

abonados = []

for i in range(CAPACIDAD):
    estado = 'Disponible'
    if len(abonados) < CAPACIDAD * PORC_FUERA_DE_SERVICIO:
        estado = 'Fuera de servicio'
    if CAPACIDAD * PORC_FUERA_DE_SERVICIO <= len(abonados) < ((CAPACIDAD * PORC_OCUPADO) + (CAPACIDAD * PORC_FUERA_DE_SERVICIO)):
        estado = 'Ocupado'
    abonado = Abonado(random.randint(3100000000, 3230000000), 'Abonado ' + str(i+1), estado)
    abonados.append(abonado)

for abonado in abonados:
    abonado.mostrarDatos()

ventana = Tk()
ventana.title("Central Telefónica")
ventana.resizable(False, False)
telefono = Telefono(ventana)
telefono.listaAbonados(abonados)
ventana.mainloop()