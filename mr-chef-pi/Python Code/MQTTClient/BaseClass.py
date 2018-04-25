import MQTTClient as Client
import time
if __name__ == '__main__':
    mr_chef = Client.MQTTClient("Mr. Chef")
    mr_chef.get_connection("192.168.137.225", 1883)
    message = "======="
    topic = "test/topic"
    mr_chef.get_subscription(topic)
    mr_chef.publish(topic, message)
    mr_chef.get_client().loop_forever()
