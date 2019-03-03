import pika


def call_back(channel, method, properties, body):
    print(body.decode('utf-8'))
    channel.basic_ack(delivery_tag=method.delivery_tag)


def listen(uri, username, password, queue_name):
    user = pika.PlainCredentials(username, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(uri, credentials=user))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        call_back,
        queue=queue_name
    )
    channel.start_consuming()
