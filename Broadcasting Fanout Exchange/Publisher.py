import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()
channel.exchange_declare(exchange='br_exchange', exchange_type='fanout')

for i in range(4):
    message = "Hello " + str(i+1)
    channel.basic_publish(exchange='br_exchange', routing_key='', body=message)
    print('[x]', message, 'sent')

channel.exchange_delete(exchange='br_exchange', if_unused=False)
