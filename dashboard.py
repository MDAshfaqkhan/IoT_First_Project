import streamlit as st
import pandas as pd
import sqlite3

DB_FILE = "sensor_data.db"

def fetch_data():
    """Fetch latest sensor data from SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 20", conn)
    conn.close()
    return df

st.title("IoT Sensor Data Dashboard")

while True:
    data = fetch_data()
    if not data.empty:
        st.write("### Latest Sensor Data")
        st.dataframe(data)

        st.write("### Temperature Over Time")
        st.line_chart(data[["timestamp", "temperature"]].set_index("timestamp"))

        st.write("### Humidity Over Time")
        st.line_chart(data[["timestamp", "humidity"]].set_index("timestamp"))
    else:
        st.warning("No data received yet. Start the MQTT publisher.")

    st.rerun()
