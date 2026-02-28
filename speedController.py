from machine import Pin, PWM
import dht
import time

# Initialize DHT11 sensor
dht_sensor = dht.DHT11(Pin(16))  # DHT11 connected to GPIO 16

# Initialize fan control (PWM)
fan = PWM(Pin(15))  # Fan control on GPIO 15
fan.freq(25000)  # Set PWM frequency to 25kHz

def set_speed(duty_cycle):
    """Set fan speed using PWM (duty cycle: 0-65535)"""
    fan.duty_u16(duty_cycle)

while True:
    try:
        dht_sensor.measure()  # Get temperature & humidity
        temp = dht_sensor.temperature()
        print(f"Temperature: {temp}°C")
        
        # Set fan speed based on temperature
        if temp < 25:
            set_speed(0)  # Fan OFF
        elif temp < 30:
            set_speed(20000)  # 30% Speed
        elif temp < 35:
            set_speed(40000)  # 60% Speed
        else:
            set_speed(65535)  # 100% Speed

        time.sleep(2)  # Wait before next reading

    except Exception as e:
        print("Error:", e)
        time.sleep(2)
1