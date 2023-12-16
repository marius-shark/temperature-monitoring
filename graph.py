import time
import adafruit_dht
import matplotlib.pyplot as plt
import board

dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

plt.ion()

x = []
y = []

def graph(temp):
  y.append(temp)
  x.append(time.time())
  plt.clf()
  plt.scatter(x,y)
  plt.plot(x,y)
  plt.draw()

while True:
     try:   
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        graph(temperature_c)
        graph(humidity)
     except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
     except Exception as error:
        dhtDevice.exit()
        raise error
     
     time.sleep(2)
