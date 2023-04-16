from app.services.MessagePusher import message_pusher


class MainClass:

    def start_publishing(self):
        message_pusher.push_messages(1, 100)


main_obj = MainClass()
main_obj.start_publishing()
