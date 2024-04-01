import smbus
import time

# Asumiendo que el PCF8591 está en la dirección 0x48
address = 0x48
bus = smbus.SMBus(1)  # Usando I2C bus 1


# Función para leer datos del ADC
def read_adc(channel):
    if channel in [0, 1, 2, 3]:
        bus.write_byte(address, 0x40 + channel)
        bus.read_byte(address)  # dummy read para iniciar la conversión
        return bus.read_byte(address)
    else:
        return None


# Lee el valor del canal al que está conectada la batería
while True:
    voltage = read_adc(0)  # Asumiendo que la batería está conectada al canal 0
    print("Voltaje leído:", voltage)
    time.sleep(1)
