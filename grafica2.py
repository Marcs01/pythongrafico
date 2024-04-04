import smbus2
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation

fields = ['X', 'Y', 'Z']
cantidad = {'X': [], 'Y': [], 'Z': []}
# altura_fija = 100

# Dirección del sensor QMC5883L
QMC5883L_ADDRESS = 0x0D

# Registro de modo
MODE_REGISTER = 0x09

# Modo de operación continuo
CONTINUOUS_MODE = 0x01

# Inicialización del bus I2C
bus = smbus2.SMBus(1)

# Configurar el modo continuo
bus.write_byte_data(QMC5883L_ADDRESS, MODE_REGISTER, CONTINUOUS_MODE)


def actualizar_datos(frame):
    # Leer datos de los registros del sensor
    data = bus.read_i2c_block_data(QMC5883L_ADDRESS, 0x00, 6)

    # Convertir los datos brutos en valores de campo magnético
    x = (data[1] << 8) | data[0]
    z = (data[3] << 8) | data[2]
    y = (data[5] << 8) | data[4]
    
    if x > 32767:
        x -= 65536
    if y > 32767:
        y -= 65536
    if z > 32767:
        z -= 65536

    # Agregar los nuevos datos a la lista
    cantidad['X'].append(x / 100)
    cantidad['Y'].append(y / 100)
    cantidad['Z'].append(z / 100)

    # Limitar la cantidad de datos mostrados para mantener la gráfica legible
    max_datos_mostrados = 20
    for field in fields:
        cantidad[field] = cantidad[field][-max_datos_mostrados:]

    # Limpiar la gráfica
    plt.clf()

    # Crear la gráfica de puntos y líneas actualizada
    for field in fields:
        plt.plot(cantidad[field], label=f'{field}: {cantidad[field][-1]}')

    # Establecer los límites de los ejes y mantener la altura fija
    
    # plt.ylim(0, altura_fija)

    # Añadir etiquetas y título
    plt.xlabel('Muestras')
    plt.ylabel('Campo Magnético')
    plt.title('Gráfico de Puntos y Líneas')
    plt.legend()

# Crear la animación con save_count
ani = animation.FuncAnimation(plt.gcf(), actualizar_datos, interval=200, save_count=10)

# Mostrar la animación
plt.show()
plt.close()
