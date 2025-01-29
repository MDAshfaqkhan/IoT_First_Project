import paho.mqtt.client as mqtt
import json
import sqlite3

BROKER = "broker.hivemq.com"
TOPIC = "iot/sensor/data"
DB_FILE = "sensor_data.db"

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            humidity REAL,
            motion INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(data):
    """Stores received sensor data in SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sensor_data (temperature, humidity, motion) VALUES (?, ?, ?)", 
                   (data["temperature"], data["humidity"], data["motion"]))
    conn.commit()
    conn.close()

def on_message(client, userdata, msg):
    """Callback function when a message is received."""
    try:
        sensor_data = json.loads(msg.payload.decode())
        print(f"Received: {sensor_data}")
        save_to_db(sensor_data)
    except json.JSONDecodeError:
        print("Error decoding JSON data")

def main():
    init_db()
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER, 1883, 60)
    client.subscribe(TOPIC)
    
    print("Listening for sensor data...")
    client.loop_forever()

if __name__ == "__main__":
    main()
