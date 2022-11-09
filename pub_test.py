
#----------------shit code ahead---------------------------------

import time
import paho.mqtt.client as paho
from paho import mqtt
# print("enter data to be sent: ")
# k=input()

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))
    print("congrats!!! msg published")

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
    print("successfully subbed")
    print("waiting for messages............")

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " +"message received = " + " " + str(msg.payload))


# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection

client.connect("10.20.44.92", 1174)

# setting callbacks, use separate functions
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish
# client.loop_start()

# client.subscribe("dev/sen1", qos=0)

# a single publish, this can also be done in loops, etc.
def pub(topic,msg):

    client.publish(topic, payload=msg, qos=0)
    
    # client.loop_forever()
def sub(topic):

    client.subscribe(topic, qos=0)
    client.loop_forever()

# client.loop_start()




# client.loop_forever()

#----------------main------------

try:

    while True:

        print("enter the function to be performed: ")
        print("subscribe (sub) or publish (pub):")
        k=input()
        if k=="pub":
            topic=input("enter topic to publis: ")
            msg=input("enter the msg to sent: ")
            pub(topic,msg)
        elif k=="sub":
            topic=input("enter topic to publish: ")
            sub(topic)
except:
    print("there is err!")

