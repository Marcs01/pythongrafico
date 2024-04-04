import smbus
import math
import time

# Dirección del sensor QMC5883 en el bus I2C
QMC5883_ADDRESS = 0x0D

# Registro de control
QMC5883_CONTROL_REGISTER = 0x09

# Registro de datos X
QMC5883_DATA_X_LSB_REGISTER = 0x00
QMC5883_DATA_X_MSB_REGISTER = 0x01

# Registro de datos Y
QMC5883_DATA_Y_LSB_REGISTER = 0x02
QMC5883_DATA_Y_MSB_REGISTER = 0x03

# Registro de datos Z
QMC5883_DATA_Z_LSB_REGISTER = 0x04
QMC5883_DATA_Z_MSB_REGISTER = 0x05

# Configuración del bus I2C
bus = smbus.SMBus(1)

# Inicializar el sensor QMC5883
bus.write_byte_data(QMC5883_ADDRESS, QMC5883_CONTROL_REGISTER, 0x1D)

# Función para leer los valores del sensor
def read_raw_data(register):
    low = bus.read_byte_data(QMC5883_ADDRESS, register)
    high = bus.read_byte_data(QMC5883_ADDRESS, register + 1)
    value = (high << 8) | low
    if value > 32767:
        value -= 65536
    return value

# Función para calcular la intensidad del campo magnético
def calculate_magnetic_intensity(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)

# Umbral de detección
UMBRAL_DETECCION = 100  # Ajusta este valor según tus necesidades

try:
    while True:
        # Leer los valores X, Y y Z del sensor
        raw_x = read_raw_data(QMC5883_DATA_X_LSB_REGISTER)
        raw_y = read_raw_data(QMC5883_DATA_Y_LSB_REGISTER)
        raw_z = read_raw_data(QMC5883_DATA_Z_LSB_REGISTER)

        # Calcular la intensidad del campo magnético
        magnetic_intensity = calculate_magnetic_intensity(raw_x, raw_y, raw_z)

        # Verificar si la intensidad es superior al umbral de detección
        if magnetic_intensity > UMBRAL_DETECCION:
            print("Objeto detectado a una distancia corta.")
        else:
            print('Nada')

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Programa detenido por el usuario.")
