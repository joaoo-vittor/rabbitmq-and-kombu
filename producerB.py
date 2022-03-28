from kombu import Connection, Exchange, Queue, Producer

rabbit_url = "amqp://guest:guest@localhost:5672//"

conn = Connection(rabbit_url)

channel = conn.channel()

exchange = Exchange("example-exchange", type="direct")


queue = Queue(name="queue2", exchange=exchange, routing_key="JOAO")
queue.maybe_bind(conn)
queue.declare()


def publish(msg, key="JOAO"):
    producer = Producer(exchange=exchange, channel=channel, routing_key=key)
    producer.publish(msg)


publish("Olá mundo, João.", "JOAO")
