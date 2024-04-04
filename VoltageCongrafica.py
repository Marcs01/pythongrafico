from tkinter import Tk, Label
import smbus2 as smbus
from datetime import datetime
import json
import os

# Configuración inicial para SMBus
bus = smbus.SMBus(1)


def setup(Addr):
    global address
    address = Addr


def read(chn):
    try:
        bus.write_byte(address, 0x40 + chn)
        bus.read_byte(address)  # Dummy read para iniciar la conversión
        value = bus.read_byte(address)
        voltage = (value / 255.0) * 3.3
        return voltage
    except Exception as e:
        print(f"Error en el canal {chn}: {e}")
        return 0


def guardar_registro(duracion):
    filename = "datosEntrada.json"
    data = {"duracion": duracion, "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r") as archivo:
            datos = json.load(archivo)
    else:
        datos = []

    datos.append(data)

    with open(filename, "w") as archivo:
        json.dump(datos, archivo, indent=4)


def verificar_voltaje():
    global contador, tolerancia
    voltage0 = read(0)
    voltage1 = read(1)

    # Actualizar la GUI con los valores actuales
    voltage0_label.config(text=f"Voltage 0: {voltage0:.9f} V")
    voltage1_label.config(text=f"Voltage 1: {voltage1:.3f} V")

    if voltage0 > 0.2:
        contador += 1
        if contador >= 5:  # Ejemplo de condición para realizar una acción
            guardar_registro(contador)
            contador = 0  # Resetear contador después de guardar
            tolerancia = 5  # Restablecer tolerancia si es parte de tu lógica
        # Espera adicional si es necesario, usando after para no bloquear
        root.after(500, verificar_voltaje)  # Esperar 500 ms antes de la próxima lectura
    else:
        contador = 0  # Resetear contador si el voltaje es bajo
        root.after(
            500, verificar_voltaje
        )  # Continuar inmediatamente si no se cumple la condición


if __name__ == "__main__":
    setup(0x48)
    tolerancia = 5
    contador = 0

    root = Tk()
    root.title("Lectura de Voltajes")

    voltage0_label = Label(root, text="Voltage 0: 0 V")
    voltage0_label.pack()

    voltage1_label = Label(root, text="Voltage 1: 0 V")
    voltage1_label.pack()

    verificar_voltaje()  # Inicia la verificación de voltaje

    root.mainloop()
