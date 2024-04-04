import smbus2
import time

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

try:
    while True:
        # Leer datos de los registros del sensor
        data = bus.read_i2c_block_data(QMC5883L_ADDRESS, 0x00, 6)
        
        # Convertir los datos brutos en valores de campo magnético
        x = (data[1] << 8) | data[0]
        z = (data[3] << 8) | data[2]
        y = (data[5] << 8) | data[4]
        
        # Calcular el campo electromagnetico
        
        
        print(data)
        
        # Esperar un momento antes de leer nuevamente
        time.sleep(.3)
except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")
