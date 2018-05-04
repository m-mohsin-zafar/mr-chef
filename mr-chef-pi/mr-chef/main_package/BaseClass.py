from Cook import Cook
from MQTTClient import MQTTClient as Client
if __name__ == '__main__':
    cook = Cook.Cook()
    mr_chef = Client.MQTTClient("Mr. Chef", cook)
    mr_chef.get_connection("192.168.8.185", 1883)
    message = ""
    topic1 = "mr-chef/update_recipe"
    topic2 = "mr-chef/connection"
    topic3 = "mr-chef/init_cooking"
    mr_chef.get_subscription(topic1)
    mr_chef.get_subscription(topic2)
    mr_chef.get_subscription(topic3)
    mr_chef.get_client().loop_forever()
