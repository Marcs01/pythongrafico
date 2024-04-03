import smbus2 as smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

def setup(Addr):
    global address
    address = Addr

def read(chn): # channel
    try:
        if chn == 0:
            bus.write_byte(address,0x40)
        if chn == 1:
            bus.write_byte(address,0x41)
        if chn == 2:
            bus.write_byte(address,0x42)
        if chn == 3:
            bus.write_byte(address,0x43)
        bus.read_byte(address) # dummy read to start conversion
    except Exception as e:
        print ("Address: %s" % address)
        print (e)
    value = bus.read_byte(address)
    # Convertir el valor leído a voltaje
    voltage = (value / 255.0) * 3.3
    return voltage

def write(val):
    try:
        temp = val # move string value to temp
        temp = int(temp) # change string to integer
        # print temp to see on terminal else comment out
        bus.write_byte_data(address, 0x40, temp)
    except Exception as e:
        print ("Error: Device address: 0x%2X" % address)
        print (e)

if __name__ == "__main__":
    setup(0x48)
    while True:
        
        tolerancia = 5
        contador = 0
        
        voltage0 = read(0)
        voltage1 = voltage0
        voltage0 = '{:.9f}'.format(voltage0)
        print ('AIN0 = ', voltage0, 'V')
        
        time.sleep(.5)
        
        if voltage1 > .2:
            
            time.sleep(.5)
            
            tmp = read(0)
            
            if(tmp > .2):
                while tolerancia > 0: 
                    voltage1 =read(0)
                    contador += 1
                
                    print('Tolerancia', tolerancia)
                    print('es mayor que .2')
            
                    if(voltage1 < .1):
                        tolerancia -=1
                    elif voltage1 >= .2:
                        tolerancia = 5
                
                
                    time.sleep(1)
                        
                    print('Duracion', contador)
                
                # Guardar el registro
                
        
        #voltage1 = read(1)
        #voltage1 = '{:.3f}'.format(voltage1)
        #print ('Voltage = ', voltage1 , 'V')
        
            # No es necesario ajustar el valor para la escritura de LED aquí,
        # a menos que estés controlando un LED con este script y quieras
        # mantener esa funcionalidad.
        
        
