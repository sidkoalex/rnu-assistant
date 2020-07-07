import os
import pathlib
from json import dumps
from os.path import dirname, join
import time

import requests
from kafka import KafkaProducer, KafkaConsumer
from pydub import AudioSegment
from pydub.playback import play

producer = None
consumer = None
while producer is None and consumer is None:
    print("Connecting to Kafka...")
    producer = KafkaProducer(bootstrap_servers=[f'localhost:29092'],
                             value_serializer=lambda x: dumps(x).encode('utf-8'))  # decode json
    consumer = KafkaConsumer('say',
                             bootstrap_servers=[f'localhost:29092'],
                             value_deserializer=lambda x: x.decode('utf-8'))  # decode plain string
    time.sleep(5)

print("Start listening messages from 'say' topic")

os.makedirs('tmp', exist_ok=True)

for message in consumer:
    payload = message.value
    print("Got message: {}".format(payload))

    response = requests.get('http://localhost:5050', {
        'voice': 'Aleksandr',  # russian man voice name
        # 'voice': 'Anna',  # russian female voice name
        # 'voice': 'Elena',  # russian female voice name
        'text': payload
    })

    fileName = join(dirname(__file__), f'tmp/voice_{time.time()}.mp3')

    with open(fileName, 'wb') as f:
        f.write(response.content)

    audio = AudioSegment.from_mp3(fileName)
    play(audio)
