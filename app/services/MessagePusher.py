from app.utils.queue import QueueConnector


def get_routing_key(number):
    if number % 2 == 0:
        return 'real-time-altair'
    else:
        return 'real-time-pollux'


class Producer:
    def __init__(self):
        self.RabbitMqConnector = QueueConnector()
        print("Producer Object Initiated.............")

    def push_messages(self, lower_limit, upper_limit):
        count = lower_limit
        while count <= upper_limit:
            routing_key = get_routing_key(count)
            msg = {"number": count, "routing_key": routing_key}
            self.RabbitMqConnector.publish_data_to_exchange(msg, routing_key)
            count += 1


message_pusher = Producer()
