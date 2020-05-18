from io import BytesIO
from json import dumps, loads

import requests
from kafka import KafkaProducer, KafkaConsumer
from pydub import AudioSegment
from pydub.playback import play

producer = KafkaProducer(bootstrap_servers=[f'localhost:29092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

consumer = KafkaConsumer(
    'say',
    bootstrap_servers=[f'localhost:29092'],
    value_deserializer=lambda x: loads(x.decode('utf-8')))

print("Start reading messages from say topic")
for message in consumer:
    payload = message.value
    print("Got message: {}".format(payload))

    r = requests.get('http://localhost:5050', {
        'voice': 'Aleksandr',
        'text': payload
    })

    # with open('voice.mp3', 'wb') as f:
    #     f.write(r.content)

    play(AudioSegment.from_mp3(BytesIO(r)))
