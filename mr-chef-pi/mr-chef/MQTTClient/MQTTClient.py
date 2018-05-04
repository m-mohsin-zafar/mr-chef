import paho.mqtt.client as mqtt
from Databases import Database as db
from Firebase import Fetch_Recipe as fr

class MQTTClient:

    def __init__(self, client_name, cook):
        self.cook = cook
        self.client = mqtt.Client(client_name)
        self.client.on_log = self.on_log
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_subscribe = self.on_subscribe

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to Broker!")
        else:
            print("Bad Connection returned code="+str(rc))

    def on_message(self, client, userdata, msg):
        if str(msg.payload.decode('utf-8')).split(" ")[0] == 'update':
            rcp = fr.fetchRecipe('https://mrchef-9eca9.firebaseio.com/')
            database = db.Database()
            conn = database.open_dbconneciton("mr-chef-db")
            if(database.insert_recipe(conn, rcp.get_recipe(str(msg.payload.decode('utf-8')).split(" ")[1]))):
                print("Database Updated")
            else:
                print("Database Couldn't be updated!")
            database.close_dbconnection(conn)
        elif str(msg.payload.decode('utf-8')).split(" ")[0] == 'cook':
            print("Cooking Started!")
            self.cook.Start()
        elif str(msg.payload.decode('utf-8')) == 'stop cooking':
            pass
        elif str(msg.payload.decode('utf-8')) == 'check':
            self.publish("mr-chef/connection","Raspberry pi is UP!")
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
