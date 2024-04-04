import smbus2
import time
import matplotlib.pyplot as plt

SENSIBILITY_RANGE = 100

def raw_to_microteslas(raw_value):
    return (raw_value / 32768) * SENSIBILITY_RANGE

# Dirección del sensor QMC5883L
QMC5883L_ADDRESS = 0x0D

# Registro de modo
MODE_REGISTER = 0x09

# Modo de operación continuo
QMC5883L_DATA_X_LSB_REGISTER = 0x00
QMC5883L_DATA_X_MSB_REGISTER = 0x01

QMC5883L_DATA_Y_LSB_REGISTER = 0x02
QMC5883L_DATA_Y_MSB_REGISTER = 0x03

QMC5883L_DATA_Z_LSB_REGISTER = 0x04
QMC5883L_DATA_Z_MSB_REGISTER = 0x05

# Inicialización del bus I2C
bus = smbus2.SMBus(1)

# Configurar el modo continuo
bus.write_byte_data(QMC5883L_ADDRESS, MODE_REGISTER, 0x1D)

def read_