import pika
import sys
import os


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()
    channel.queue_declare(queue='test')

    def callBack(ch, method, properties, body):
        print('[x]Recieved:', body)

    channel.basic_consume(
        queue='test', on_message_callback=callBack, auto_ack=True)

    print('[*]Waiting for messages.To exit press ctrl+c')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('[!]Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
