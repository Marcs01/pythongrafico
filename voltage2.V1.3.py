import smbus2 as smbus
import time
import json
from datetime import datetime
import os
import pandas as pd
from openpyxl import load_workbook

bus = smbus.SMBus(1)

address = None


def setup(Addr):

    global address
    address = Addr


def read(chn):

    try:

        bus.write_byte(address, 0x40 + chn)
        bus.read_byte(address)

        value = bus.read_byte(address)
        voltage = (value / 255.0) * 3.3

        return voltage

    except Exception as e:

        print(f"Address: {address} Error: {e}")

        return None


def log_voltage(voltage, contador):

    nombre_archivo = datetime.today().strftime("%d-%B-%Y") + ".xlsx"

    if not os.path.exists(nombre_archivo):

        df = pd.DataFrame(
            data={
                "Voltaje": [voltage],
                "Contador": [contador],
                "Fecha": [datetime.now()],
            }
        )

        df.to_excel(nombre_archivo, index=False)

    else:

        # Si el archivo existe, carga y añade una nueva fila.
        libro = load_workbook(nombre_archivo)

        writer = pd.ExcelWriter(nombre_archivo, engine="openpyxl")
        writer.book = libro
        writer.sheets = dict((ws.title, ws) for ws in libro.worksheets)

        df = pd.read_excel(nombre_archivo)
        df = df.append(
            {"Voltaje": voltage, "Contador": contador, "Fecha": datetime.now()},
            ignore_index=True,
        )
        df.to_excel(writer, index=False)

        writer.save()


def append_data_to_json(data, file_name="datosEntrada.json"):

    if os.path.exists(file_name):

        with open(file_name, "r") as file:
            existing_data = json.load(file)

    else:

        existing_data = []

    existing_data.append(data)

    with open(file_name, "w") as file:
        json.dump(existing_data, file, indent=4)


if __name__ == "__main__":

    setup(0x48)

    datos = []

    while True:

        voltage0 = read(0)

        if voltage0 is not None and voltage0 > 0.2:

            time.sleep(0.5)
            tmp = read(0)

            if tmp > 0.2:

                contador = 0
                tolerancia = 5

                while tolerancia > 0:

                    voltage1 = read(0)
                    contador += 1

                    if voltage1 < 0.1:

                        tolerancia -= 1

                    elif voltage1 >= 0.2:

                        tolerancia = 5

                    log_voltage(voltage1, contador)
                    time.sleep(1)

                data = {
                    "duracion": contador,
                    "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }

                datos.append(data)

                append_data_to_json(data)
