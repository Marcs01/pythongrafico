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

        if voltage0 > 3.2:
            ultima_fila = None  # este el campo de la ultima fila

            tiempo_campo = datetime.now().strftime("%Y%m%d%H%M%S")
            tiempo_campo2 = tiempo_campo
            nombre_archivo = "logs/" + datetime.now().strftime("%Y%m%d") + ".csv"
            file_exists = os.path.exists(nombre_archivo)
            value = 1

            time.sleep(0.5)
            tmp = read(0)

            if tmp > 3.2:
                tiempo_campo2 = datetime.now().strftime("%Y%m%d%H%M%S")
                value = 2

            print(value)

            with open(nombre_archivo, "r") as archivo:
                if file_exists:

                    for ultima_fila in csv.reader(archivo):
                        # necesito obtener la ultima fila
                        pass
                        if ultima_fila:
                            print(ultima_fila)

            with open(nombre_archivo, mode="a") as archivo:
                writer = csv.writer(archivo)
                if not file_exists:
                    writer.writerow(["bird_duration", "value"])
                data = [tiempo_campo2, value]
                writer.writerow(data)
