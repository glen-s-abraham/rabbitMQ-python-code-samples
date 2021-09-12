import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()
channel.exchange_declare(exchange='br_exchange', exchange_type='fanout')
res = channel.queue_declare(queue='', exclusive=True)
queue_name = res.method.queue
print('Subscriber queue name', queue_name)
channel.queue_bind(exchange='br_exchange', queue=queue_name)
print('[*] Waiting for messages')


def callBack(ch, method, properties, body):
    print('[x] ', body)


channel.basic_consume(
    queue=queue_name, on_message_callback=callBack, auto_ack=True)

channel.start_consuming()
