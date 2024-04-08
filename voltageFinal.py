import smbus2 as smbus
import time
import csv
from datetime import datetime
import os

bus = smbus.SMBus(1)


def eliminar_y_escribir(nombre_archivo, datos, fila_nueva):
    """Elimina la última fila si es necesario y escribe los datos modificados de vuelta al archivo."""
    with open(
        nombre_archivo,
        "w",
    ) as archivo:
        writer = csv.writer(archivo)
        if not datos:
            writer.writerow(
                ["bird_duration", "value"]
            )  # Escribir cabecera si es un archivo nuevo
        else:
            writer.writerows(
                datos
            )  # Escribir datos existentes (sin la última fila si se modificó)
        writer.writerow(fila_nueva)  # Escribir la nueva fila


def setup(Addr):

    global address
    address = Addr


def read(chn):

    try:

        if chn == 0:
            bus.write_byte(address, 0x40)
        if chn == 1:
            bus.write_byte(address, 0x41)
        if chn == 2:
            bus.write_byte(address, 0x42)
        if chn == 3:
            bus.write_byte(address, 0x43)
        bus.read_byte(address)

    except Exception as e:

        print("Address: %s" % address)
        print(e)

    value = bus.read_byte(address)
    voltage = (value / 255.0) * 3.3

    return voltage


def write(val):

    try:

        temp = val
        temp = int(temp)
        bus.write_byte_data(address, 0x40, temp)

    except Exception as e:

        print("Error: Device address: 0x%2X" % address)
        print(e)


if __name__ == "__main__":
    setup(0x48)

    while True:
        voltage0 = read(0)
        print("{:.9f}".format(voltage0))
        time.sleep(0.5)

        tiempo_campo = datetime.now().strftime("%Y%m%d%H%M%S")
        nombre_archivo = "logs/" + datetime.now().strftime("%Y%m%d") + ".csv"
        file_exists = os.path.exists(nombre_archivo)
        value = 1

        if voltage0 > 3.2:
            value = 2

        datos_modificados = []
        if file_exists:
            # Leer y almacenar todos los datos
            with open(nombre_archivo, "r", newline="") as archivo:
                datos_modificados = list(csv.reader(archivo))

            # Verificar la condición y modificar los datos si es necesario
            if datos_modificados and datos_modificados[-1][0] == tiempo_campo:
                # La condición para modificar/eliminar la última fila va aquí.
                # En este caso, simplemente eliminamos la última fila.
                datos_modificados.pop()

        # La nueva fila a añadir
        fila_nueva = [tiempo_campo, value]

        # Escribir los datos modificados de vuelta al archivo (sin la última fila si se eliminó) y añadir la nueva fila
        eliminar_y_escribir(nombre_archivo, datos_modificados, fila_nueva)

        # Espera antes de la siguiente medición
        time.sleep(1)
