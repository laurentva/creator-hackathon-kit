API_KEY = "030d3ab9-df02-4213-83de-90b31b86920a"
TOPIC = "5abca60f0e091b0005581409"

import paho.mqtt.client as mqtt
import ssl
import json


host = "mqtt.cloud.pozyxlabs.com"
port = 443
username = TOPIC
password = API_KEY


def on_connect(client, userdata, flags, rc):
    print(mqtt.connack_string(rc))


def on_message(client, userdata, msg):
    tag_data = json.loads(msg.payload.decode())
    
    for tag in tag_data:
        try:
            if tag["success"]:
                network_id = tag["tagId"]
                position = tag["data"]["coordinates"]

                print(network_id, position)
                # YOUR CODE GOES HERE
        except KeyError:
            pass


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic!")


client = mqtt.Client(transport="websockets")

client.username_pw_set(username, password=password)

client.tls_set_context(context=ssl.create_default_context())

client.on_connect = on_connect

client.on_message = on_message
client.on_subscribe = on_subscribe

client.connect(host, port=port)
client.subscribe(TOPIC)

client.loop_forever()
