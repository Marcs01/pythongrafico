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
                [
                    "",
                ]
            )
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
    nombre_archivo = "logs/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".csv"

    while True:
        voltage0 = read(0)
        print("{:.9f}".format(voltage0))
        time.sleep(0.5)

        file_exists = os.path.exists(nombre_archivo)

        if voltage0 > 2:
            tiempo_campo = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

            # time.sleep(0.5)
            voltage1 = read(0)
            with open(nombre_archivo, mode="a") as archivo:
                writer = csv.writer(archivo)
                if not file_exists:
                    writer.writerow([])
                data = [tiempo_campo]
                writer.writerow(data)
