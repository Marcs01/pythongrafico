import time
import board
import busio
import adafruit_mpr121
import csv
import datetime

# Inicializar la comunicación I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Crear una instancia del objeto MPR121
mpr121 = adafruit_mpr121.MPR121(i2c)

# Crear un archivo CSV para guardar los datos
file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"

def setup():
    # Crear un archivo CSV para guardar los datos
    mpr121[9].threshold(12)
    mpr121[9].release_threshold(6)

    with open(file_name, 'w', newline='') as file:

        writer = csv.writer(file)
        writer.writerow(["Timestamp"])

def log_event(event_timestamp):
    # Log the event in the CSV file
    with open(file_name, 'a', newline='') as file:

        writer = csv.writer(file)
        writer.writerow([event_timestamp])



# Bucle principal
if __name__ == '__main__':
    setup()
    tmp = None

    try:

        while True:
 
            if mpr121[9].value:  # Object detected
                current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if tmp != current_timestamp:
                    tmp = None

                if tmp is None:
                    log_event(current_timestamp)  # Log the detection immediately
                    tmp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
                print("Object detected", current_timestamp)
            else:  # No object detected
                print("No object detected")
                    
                    

            time.sleep(.1)

    except KeyboardInterrupt:
        pass
    finally:
        pass
