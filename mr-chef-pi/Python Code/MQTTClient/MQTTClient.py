import paho.mqtt.client as mqtt


class MQTTClient:

    def __init__(self, client_name):
        self.client = mqtt.Client(client_name)
        self.client.on_log = self.on_log
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_subscribe = self.on_subscribe

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connection OK")
        else:
            print("Bad Connection returned code="+str(rc))

    def on_message(self, client, userdata, msg):
        if str(msg.payload.decode('utf-8')) == 'hi':
            self.publish(msg.topic, 'hello')
        if str(msg.payload.decode('utf-8')) == 'how are you?':
            self.publish(msg.topic, 'Im fine and how are you?')
        # print("Topic: " + msg.topic + "\nMessage: " + str(msg.payload.decode('utf-8')))

    def on_publish(self, client, userdata, mid):
        print("In on_pub callback mid="+str(mid))

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed")

    def on_log(self, client, userdata, level, buf):
        print(buf)

    def on_disconnect(self, client, userdata, rc):
        print("Disconnection OK")

    def get_connection(self, broker, port):
        try:
            self.client.connect(broker, port)
        except ConnectionError:
            print("Sorry, Cannot connect! Broker is down")

    def get_subscription(self, topic):
        self.client.subscribe(topic)

    def publish(self, topic, message):
        self.client.publish(topic, message)

    def disconnect(self):
        self.client.disconnect()

    def get_client(self):
        return self.client
