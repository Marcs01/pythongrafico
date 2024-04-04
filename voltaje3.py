import smbus2 as smbus
import time

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
        print("Address: %s" % address)
        print(e)
    value = bus.read_byte(address)
    # Convertir el valor leído a voltaje utilizando la resolución del ADC
    voltage = value
    return voltage

def write(val):
    try:
        temp = int(val) # change string to integer
        bus.write_byte_data(address, 0x40, temp)
    except Exception as e:
        print("Error: Device address: 0x%2X" % address)
        print(e)

if __name__ == "__main__":
    setup(0x48)
    while True:
        # voltage0 = read(0)
        #print('AIN0 = ', voltage0, 'V')
        voltage1 = read(1)
        voltage1 = "{:.3f}".format(voltage1)
        print('AIN1 = ', voltage1 )
        time.sleep(0.3)