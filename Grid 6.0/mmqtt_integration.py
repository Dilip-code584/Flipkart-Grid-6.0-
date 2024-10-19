import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("warehouse/sensor_data")

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Update the broker address and port if needed
client.connect("broker.hivemq.com", 1883, 60)

# Simulating a sensor reading
client.publish("warehouse/sensor_data", "Temperature: 22.5C")

client.loop_forever()

