import smbus
import time

# Crea una instancia de la clase SMBus para acceder al bus I2C.
# El número '1' indica que estamos usando el bus I2C número 1.
bus = smbus.SMBus(1)

# Dirección I2C del módulo PCF8591.
direccion_pcf8591 = 0x48  # Puede variar, revisa la documentación de tu módulo.

                                          
def leer_canal(canal):
    
    bus.write_byte(direccion_pcf8591, 0x40 + canal)
    time.sleep(0.1)
    valor = bus.read_byte(direccion_pcf8591)
    return valor

# Ciclo infinito para leer el valor del sensor Hall y mostrarlo.
while True:
    valor_sensor = leer_canal(1)  # Cambia '0' por el canal que estés usando (0-3).
    print("Valor del sensor Hall:", valor_sensor)
    time.sleep(.2)
