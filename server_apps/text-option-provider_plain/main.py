import logging
from json import dumps, loads
from os import getenv

from kafka import KafkaProducer, KafkaConsumer

####################
# Initializing
####################

APP_NAME = getenv("APP_NAME", "text-option-provider_plain")
GROUP_NAME = getenv("GROUP_NAME", "text-option-provider")
LOG_LEVEL = getenv("LOG_LEVEL", "DEBUG")

MESSAGING_RECEIVE_TOPIC_NAME = getenv('MESSAGING_RECEIVE_TOPIC_NAME', 'user-request-listener')
MESSAGING_SEND_TOPIC_NAME = getenv('MESSAGING_SEND_TOPIC_NAME', 'text-option-provider')
MESSAGING_HOST = getenv('MESSAGING_HOST', 'kafka')
MESSAGING_PORT = getenv('MESSAGING_PORT', '9092')

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

        answer = {
            'user_request_id': payload['user_request_id'],
            'request_text': payload['user_request_text']
        }
        send_answer_message(answer)
