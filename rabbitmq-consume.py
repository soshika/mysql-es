import pika
import json
import requests


# variables goes here ...
###########################

API_METHOD = 'POST'
QUEUE_NAME = 'maxwell-queue'
RABBIT_MQ_HOST = 'localhost'
API_URL = 'http://fastmovie.online:9091/es'

###########################


# function goes here ...
###########################

def req(body):
    url = API_URL
    payload = json.dumps(body)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request(API_METHOD, url, headers=headers, data=payload)

    from pprint import pprint
    pprint(response)


def callback(ch, method, properties, body):
    json_body = json.loads(str(body, 'utf-8'))
    req(json_body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


###########################


if __name__ == '__main__':
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_MQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    channel.start_consuming()