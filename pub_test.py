
# #----------------shit code ahead---------------------------------

# import time
# import paho.mqtt.client as paho
# from paho import mqtt
# # print("enter data to be sent: ")
# # k=input()

# # setting callbacks for different events to see if it works, print the message etc.
# def on_connect(client, userdata, flags, rc, properties=None):
#     print("CONNACK received with code %s." % rc)

# # with this callback you can see if your publish was successful
# def on_publish(client, userdata, mid, properties=None):
#     print("mid: " + str(mid))
#     print("congrats!!! msg published")

# # print which topic was subscribed to
# def on_subscribe(client, userdata, mid, granted_qos, properties=None):
#     print("Subscribed: " + str(mid) + " " + str(granted_qos))
#     print("successfully subbed")
#     print("waiting for messages............")

# # print message, useful for checking if it was successful
# def on_message(client, userdata, msg):
#     print(msg.topic + " " +"message received = " + " " + str(msg.payload))


# # userdata is user defined data of any type, updated by user_data_set()
# # client_id is the given name of the client
# client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
# client.on_connect = on_connect

# # enable TLS for secure connection

# client.connect("10.20.44.92", 1174)

# # setting callbacks, use separate functions
# client.on_subscribe = on_subscribe
# client.on_message = on_message
# client.on_publish = on_publish
# # client.loop_start()

# # client.subscribe("dev/sen1", qos=0)

# # a single publish, this can also be done in loops, etc.
# def pub(topic,msg):

#     client.publish(topic, payload=msg, qos=0)
    
#     # client.loop_forever()
# def sub(topic):

#     client.subscribe(topic, qos=0)
#     client.loop_forever()

# # client.loop_start()




# # client.loop_forever()

# #----------------main------------

# try:

#     while True:

#         print("enter the function to be performed: ")
#         print("subscribe (sub) or publish (pub):")
#         k=input()
#         if k=="pub":
#             topic=input("enter topic to publis: ")
#             msg=input("enter the msg to sent: ")
#             pub(topic,msg)
#         elif k=="sub":
#             topic=input("enter topic to publish: ")
#             sub(topic)
# except:
#     print("there is err!")

import paho.mqtt.client as mqtt #import the client1
import time

broker = "10.20.23.196"
port = 1881

def on_connect(client, userdata, flags, rc, properties=None):
    print("connected with response code %s" %rc)

def on_publish(client, userdata, mid):
    print("mid/response = " + str(mid))
    print("published successfully")

def on_subscribe(client, userdata, mid, granted_qos):
    print("mid/response = " + str(mid))
    print("subscribed successfully with qos " + str(granted_qos))

def on_message(client, userdata, message):
    print("received message: ")
    print("\t payload: " + str(message.payload) + "\n \t topic: " + str(message.topic))
    print("\t qos: " + str(message.qos))

def on_log(client, userdata, level, buf):
    print(buf)

def pub(topic, message, iqos):
    client.publish(topic, payload=message, qos=iqos)

def sub(topic, iqos):
    client.subscribe(topic, qos=iqos)
    # client.loop_forever()


client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv31)
client.on_connect = on_connect

client.connect(broker, port)
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_log = on_log
client.loop_start()

try:
    
    query = input("pub or sub? ")
    if query == "pub":
        
        topic = input("topic: ")
        while True:
            msg = input("message: ")
            inqos = int(input("qos: "))
            pub(topic, msg, inqos)
            time.sleep(1)
    elif query == "sub":
        topic = input("topic: ")
        inqos = int(input("qos: "))
        sub(topic, inqos)
except:
    print("error")
    client.on_log


