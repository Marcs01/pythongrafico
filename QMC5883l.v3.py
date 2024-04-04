import smbus2
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json
from datetime import datetime

fields = ['X', 'Y', 'Z']
cantidad = {'X': [], 'Y': [], 'Z': []}
ultimos_valores = {'X': None, 'Y': None, 'Z': None}
umbral_cambio_significativo = 25  # Define el umbral de cambio significativo

QMC5883L_ADDRESS = 0x0D
MODE_REGISTER = 0x09
CONTINUOUS_MODE = 0x01
bus = smbus2.SMBus(1)
bus.write_byte_data(QMC5883L_ADDRESS, MODE_REGISTER, CONTINUOUS_MODE)

def es_cambio_significativo(valor_actual, valor_anterior):
    return abs(valor_actual - valor_anterior) >= umbral_cambio_significativo if valor_anterior is not None else False

def actualizar_datos(frame):
    data = bus.read_i2c_block_data(QMC5883L_ADDRESS, 0x00, 6)
    x = ((data[1] << 8) | data[0]) / 100
    z = ((data[3] << 8) | data[2]) / 100
    y = ((data[5] << 8) | data[4]) / 100
    
    if x > 327.67: x -= 655.36
    if y > 327.67: y -= 655.36
    if z > 327.67: z -= 655.36

    # Comprobar si hay un cambio significativo en cualquiera de las variables
    if any(es_cambio_significativo(v, ultimos_valores[k]) for k, v in zip(fields, [x, y, z])):
        registro = {
            "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "x": x,
            "y": y,
            "z": z
        }
        with open('cambios_significativos.json', 'a') as archivo_json:
            json.dump(registro, archivo_json)
            archivo_json.write("\n")  # Añadir una nueva línea para separar los registros
            
    # Actualizar los últimos valores registrados
    ultimos_valores['X'], ultimos_valores['Y'], ultimos_valores['Z'] = x, y, z

    # Agregar los nuevos datos a la lista para la gráfica
    cantidad['X'].append(x)
    cantidad['Y'].append(y)
    cantidad['Z'].append(z)

    max_datos_mostrados = 20
    for field in fields:
        cantidad[field] = cantidad[field][-max_datos_mostrados:]

    plt.clf()
    for field in fields:
        plt.plot(cantidad[field], label=f'{field}: {cantidad[field][-1]}')

    plt.xlabel('Muestras')
    plt.ylabel('Campo Magnético')
    plt.title('Gráfico de Puntos y Líneas')
    plt.legend()

ani = animation.FuncAnimation(plt.gcf(), actualizar_datos, interval=200, save_count=10)
plt.show()
plt.close()
