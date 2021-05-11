import paho.mqtt.client as mqtt
import time


    
def pub():
    mqttBroker ="test.mosquitto.org"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("hello esp8266",'utf-8')))     

pub()    
