import smbus2 as smbus
import time
import csv
from datetime import datetime
import os

bus = smbus.SMBus(1)


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
            value = 2  # Suponiendo que quieres cambiar a 2 directamente si el voltaje supera 3.2

            # Leer la última fila solo si el archivo existe
            ultima_fila = None
            if file_exists:
                with open(nombre_archivo, "r") as archivo:
                    datos = list(csv.reader(archivo))
                    if datos:
                        if datos[-1][0] == tiempo_campo:
                            writer = csv.writer(archivo)
                            if not file_exists:
                                writer.writerow(
                                    ["bird_duration", "value"]
                                )  # Escribir cabecera si es nuevo archivo
                            datos.pop()
                            writer.writerow(datos)

            # Ahora, escribe los datos al archivo
            with open(nombre_archivo, mode="a", newline="") as archivo:
                writer = csv.writer(archivo)
                if not file_exists:
                    writer.writerow(
                        ["bird_duration", "value"]
                    )  # Escribir cabecera si es nuevo archivo
                data = [tiempo_campo, value]
                writer.writerow(data)
