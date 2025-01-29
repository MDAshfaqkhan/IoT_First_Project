import paho.mqtt.client as mqtt
import random
import time
import json

BROKER = "broker.hivemq.com"  # Public MQTT Broker
TOPIC = "iot/sensor/data"  # Topic to publish sensor data

def generate_sensor_data():
    """Generates random sensor data (Temperature, Humidity, Motion)."""
    return {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(30, 70), 2),
        "motion": random.choice([0, 1])
    }

def main():
    client = mqtt.Client()
    client.connect(BROKER, 1883, 60)

    while True:
        sensor_data = generate_sensor_data()
        client.publish(TOPIC, json.dumps(sensor_data))  # Publish as JSON
        print(f"Published: {sensor_data}")
        time.sleep(2)

if __name__ == "__main__":
    main()
