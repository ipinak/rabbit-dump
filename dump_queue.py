import sys
import csv
import json
from pika import PlainCredentials, ConnectionParameters, BlockingConnection


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    jdata = json.loads(body)
    convert_to_csv(jdata)


def convert_to_csv(json_data):
    with open('messages.csv', 'a') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='|')
        csv_writer.writerow(json_data.values())


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print """Usage> python dump_queue.py <mq_url> <mq_user> <mq_pass>
                <mq_vhost> <mq_queue_name>"""
        exit()

    mq_url = sys.argv[1]
    mq_user = sys.argv[2]
    mq_pass = sys.argv[3]
    mq_vhost = sys.argv[4]
    mq_queue_name = sys.argv[5]

    credentials = PlainCredentials(mq_user, mq_pass)
    connection = BlockingConnection(
        ConnectionParameters(mq_url, 5672, mq_vhost, credentials))

    channel = connection.channel()
    channel.queue_declare(queue=mq_queue_name)
    channel.basic_consume(callback, queue=mq_queue_name)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
