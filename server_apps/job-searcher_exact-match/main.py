import logging
from json import loads, dumps
from os import getenv

from kafka import KafkaProducer, KafkaConsumer
from pymongo import MongoClient

####################
# Initializing
####################

APP_NAME = getenv("APP_NAME", "job-searcher_exact-match")
GROUP_NAME = getenv("GROUP_NAME", "job-searcher")
LOG_LEVEL = getenv("LOG_LEVEL", "DEBUG")

MESSAGING_RECEIVE_TOPIC_NAME = getenv('MESSAGING_RECEIVE_TOPIC_NAME', 'text-option-provider')
MESSAGING_SEND_TOPIC_NAME = getenv('MESSAGING_SEND_TOPIC_NAME', 'job-searcher')
MESSAGING_HOST = getenv('MESSAGING_HOST', 'localhost')
MESSAGING_PORT = getenv('MESSAGING_PORT', '9092')

DB_HOST = getenv("DB_HOST", 'mongo')
DB_NAME = getenv("DB_NAME", 'assistant')
DB_USER_NAME = getenv("DB_USER_NAME", 'root')
DB_PASSWORD = getenv("DB_PASSWORD", 'root')

log = logging.getLogger(APP_NAME)
log.setLevel(logging.DEBUG)
log_console_handler = logging.StreamHandler()
log_console_handler.setLevel(LOG_LEVEL)
log_formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s')
log_console_handler.setFormatter(log_formatter)
log.addHandler(log_console_handler)

log.info(f"Creating Kafka producer on {MESSAGING_HOST}:{MESSAGING_PORT}")
producer = KafkaProducer(bootstrap_servers=[f'{MESSAGING_HOST}:{MESSAGING_PORT}'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

log.info(f"Creating Kafka consumer on topic {MESSAGING_RECEIVE_TOPIC_NAME} with group_id {GROUP_NAME}")
consumer = KafkaConsumer(
    MESSAGING_RECEIVE_TOPIC_NAME,
    bootstrap_servers=[f'{MESSAGING_HOST}:{MESSAGING_PORT}'],
    group_id=GROUP_NAME,
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# Init database
db_client = MongoClient(DB_HOST, username=DB_USER_NAME, password=DB_PASSWORD)
db = db_client[DB_NAME]
job_collection = db['jobs']


####################
# Helper functions
####################

def send_answer_message(payload):
    log.debug("Sending answer message to topic %s. Message: %s", MESSAGING_SEND_TOPIC_NAME, payload)
    producer.send(MESSAGING_SEND_TOPIC_NAME, payload)


####################
# Run
####################

if __name__ == '__main__':
    log.debug("Logging DEBUG level is on")
    log.info("Start messages consuming")

    for message in consumer:
        payload = message.value
        log.debug("Got message with payload %s", payload)

        request_text = payload['request_text']

        job = job_collection.find_one({
            'search_type': 'EXACT_MATCH',
            'search_data': request_text
        })

        if job is None:
            log.debug(f"Nothing found for request_text: {request_text}")
            continue

        del job['_id']
        answer = {
            'request': payload,
            'job': job
        }
        send_answer_message(answer)
