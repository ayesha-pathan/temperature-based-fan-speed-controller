import machine
import time
import dht

# Initialize DHT11 sensor on GPIO 9
d = dht.DHT11(machine.Pin(9))

# Continuously read and print temperature and humidity
while True:
    d.measure()
    print("Temperature:", d.temperature())
    print("Humidity:", d.humidity())
    time.sleep_ms(2000)  # Read every 2 seconds