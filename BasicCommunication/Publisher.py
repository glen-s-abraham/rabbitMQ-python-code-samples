import pika

# initiate connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# create channel
channel = connection.channel()

# if queue does not exist
# create a queue through the channel
channel.queue_declare(queue='test')

# publish the message
channel.basic_publish(exchange="", routing_key="hello", body="hello world")
print('[x] Sent hello world')

# close the connection
connection.close()
