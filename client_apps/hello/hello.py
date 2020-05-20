import random
from json import dumps, loads
from time import sleep

from kafka import KafkaProducer, KafkaConsumer

producer = None
consumer = None
while producer is None and consumer is None:
    print("Connecting to Kafka...")
    producer = KafkaProducer(bootstrap_servers=[f'localhost:29092'])
    consumer = KafkaConsumer('job-searcher',
                             bootstrap_servers=[f'localhost:29092'],
                             value_deserializer=lambda x: loads(x.decode('utf-8')))
    sleep(5)

print("Start listening for messages from 'job-searcher' topic")

for message in consumer:
    payload = message.value
    print("Got message: {}".format(payload))

    if payload['job']['name'] == 'HELLO':
        hello_text = random.choice(['Привет', 'Здравствуйте', 'Рад слышать'])
        producer.send('say', hello_text.encode())
        print(f"Speaking: {hello_text}")
