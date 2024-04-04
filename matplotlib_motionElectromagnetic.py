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
CONTINUOUS_MODE = 0x01

# Inicialización del bus I2C
bus = smbus2.SMBus(1)

# Configurar el modo continuo
bus.write_byte_data(QMC5883L_ADDRESS, MODE_REGISTER, CONTINUOUS_MODE)

# Listas para almacenar los datos de campo magnético (x, y, z) y el tiempo
x_data = []
y_data = []
z_data = []
time_data = []

try:
    while True:
        # Leer datos de los registros del sensor
        data = bus.read_i2c_block_data(QMC5883L_ADDRESS, 0x00, 6)
        
        # Convertir los datos brutos en valores de campo magnético
        x = (data[1] << 8) | data[0]
        z = (data[3] << 8) | data[2]
        y = (data[5] << 8) | data[4]
        
        x = raw_to_microteslas(x)
        z = raw_to_microteslas(z)
        y = raw_to_microteslas(y)
        # Obtener el tiempo actual
        current_time = time.time()
        
        # Agregar los datos a las listas
        x_data.append(x)
        y_data.append(y)
        z_data.append(z)
        time_data.append(current_time)
        
        # Imprimir los valores del campo magnético
        print("Campo magnético (X, Y, Z): ({}, {}, {})".format(x, y, z))
        
        
        # Graficar los datos
   
            
    # Esperar un momento antes de leer nuevamente
    time.sleep(0.1)
except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")

plt.plot(time_data, x_data, label='X')
plt.plot(time_data, y_data, label='Y')
plt.plot(time_data, z_data, label='Z')
plt.xlabel('Tiempo')
plt.ylabel('Campo Magnético')
plt.title('Campo Magnético (X, Y, Z) en función del Tiempo')
plt.legend()
plt.grid(True)
plt.show()
