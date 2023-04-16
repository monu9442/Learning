import os
QUEUE_PORT = '5672'

class Queue:
    host = None
    port = None
    user = None
    password = None

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = QUEUE_PORT
        self.user = os.environ.get("QUEUE_USER", "guest")
        self.password = os.environ.get("QUEUE_PASSWORD", "guest")
        self.exchange = os.environ.get("QUEUE_EXCHANGE", 'pollux-fanout')

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_exchange(self):
        return self.exchange


QueueCredentials = Queue()
