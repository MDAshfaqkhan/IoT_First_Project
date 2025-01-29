import random
import time

def generate_sensor_data():
    while True:
        temperature = round(random.uniform(20, 35), 2)  
        humidity = round(random.uniform(30, 70), 2)     
        motion = random.choice([0, 1])                  
        
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Motion: {motion}")
        time.sleep(2)  # Data updates every 2 seconds

generate_sensor_data()
