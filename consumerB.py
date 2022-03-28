from kombu import Connection, Exchange, Queue
from kombu.mixins import ConsumerMixin

rabbit_url = "amqp://guest:guest@localhost:5672//"


class Worker(ConsumerMixin):
    def __init__(self, connection, queues):
        self.connection = connection
        self.queues = queues

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=self.queues, callbacks=[self.on_message])]

    def on_message(self, body, message):
        print("Got message: {0}".format(body))
        message.ack()


exchange = Exchange("example-exchange", type="direct")
queues = [
    Queue("queue1", exchange, routing_key="VITOR"),
    Queue("queue2", exchange, routing_key="JOAO"),
]

with Connection(rabbit_url, heartbeat=4) as conn:
    try:
        worker = Worker(conn, queues)
        print("Start consuming: ")
        worker.run()
    except:
        raise
