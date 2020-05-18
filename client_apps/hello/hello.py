import random
from json import dumps, loads

from kafka import KafkaProducer, KafkaConsumer

producer = KafkaProducer(bootstrap_servers=[f'localhost:29092'])

consumer = KafkaConsumer(
    'job-searcher',
    bootstrap_servers=[f'localhost:29092'],
    value_deserializer=lambda x: loads(x.decode('utf-8')))

print("Start reading messages from job-searcher topic")
for message in consumer:
    payload = message.value
    print("Got message: {}".format(payload))

    if 'job' not in payload:
        continue

    job = payload['job']
    if job.get('name') == 'HELLO':
        hello_text = random.choice(['Привет', 'Здравствуйте', 'Рад слышать'])
        producer.send('say', hello_text)
        print(f"Speaking: {hello_text}")
