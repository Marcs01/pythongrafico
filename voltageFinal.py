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

        tolerancia = 5
        contador = 0
        voltage0 = read(0)
        voltage1 = voltage0
        voltage0 = "{:.9f}".format(voltage0)
        print(voltage1)
        time.sleep(0.5)

        if voltage1 > 3.106:

            time.sleep(0.5)
            tmp = read(0)

            if tmp > 3.106:

                print("Es mayor a dos")

                while tolerancia > 0:

                    voltage1 = read(0)
                    contador += 1

                    if voltage1 < 3.106:
                        tolerancia -= 1
                    elif voltage1 >= 3.106:
                        tolerancia = 5

                    print(tolerancia)
                    time.sleep(1)

                nombre_archivo = datetime.now().strftime("%d-%b-%Y") + "_datos.csv"
                file_exists = os.path.exists(nombre_archivo)

                with open(nombre_archivo, mode="a", newline="") as archivo:

                    fieldnames = ["durancion", "hora"]
                    writer = csv.DictWriter(archivo, fieldnames=fieldnames)

                    if not file_exists:

                        writer.writeheader()

                    data = {
                        "durancion": contador,
                        "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }

                    writer.writerow(data)
