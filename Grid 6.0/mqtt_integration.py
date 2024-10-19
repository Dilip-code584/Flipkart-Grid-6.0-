import paho.mqtt.client as mqtt

# Create a new MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect("broker.hivemq.com", 1883, 60)

# Optional: Define a callback for successful connection
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code: {rc}")

client.on_connect = on_connect

# Start the loop to process network traffic and handle callbacks
client.loop_start()

# Optional: Publish a message
client.publish("your/topic", "Hello, MQTT!")

# Keep the script running (optional, can be replaced with your logic)
try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    # Stop the loop and disconnect when done
    client.loop_stop()
    client.disconnect()
