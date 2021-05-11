from umqtt.simple import MQTTClient

def msg(a,b):
    data=(str(b,'utf-8'))
    print(data)
    
    
def client():
    server="test.mosquitto.org"
    c = MQTTClient("umqtt_client", server)
    c.set_callback(msg)
    c.connect()
    c.subscribe("test2")
    c.wait_msg()
    c.check_msg()
    c.disconnect()
    
client()    
