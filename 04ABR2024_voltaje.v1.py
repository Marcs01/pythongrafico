import smbus
import time

address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)

while True:
    bus.read_byte_data(address, A1)  # do the measurement but ignore the value
    value = bus.read_byte_data(address, A1)  # get the correct value
    # print(value)
    print("AOUT: %1.03f" % (value * 3.3 / 255))
    time.sleep(0.2)
