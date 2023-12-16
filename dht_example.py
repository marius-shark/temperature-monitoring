import time
import board
import adafruit_dht
import os

# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D4)
 
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        f = open('/home/marius/temperature-monitoring/humidity.csv', 'a+')
        if humidity is not None and temperature_c is not None:
            f.write('{0},{1},{2:0.1f},{3:0.1f}\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature_c, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")

        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                temperature_c, humidity
            )
        )
 
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(60)


