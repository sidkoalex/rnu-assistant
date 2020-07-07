import logging
from json import dumps, loads
from os import getenv
from multiprocessing import Process
from kafka import KafkaProducer, KafkaConsumer

####################
# Configurations
####################

# App config
APP_NAME = getenv("APP_NAME", "text-option-provider_plain")
GROUP_NAME = getenv("GROUP_NAME", "text-option-provider")

# Messaging config
MESSAGING_RECEIVE_TOPIC_NAME = getenv('MESSAGING_RECEIVE_TOPIC_NAME', 'user-request-listener')
MESSAGING_SEND_TOPIC_NAME = getenv('MESSAGING_SEND_TOPIC_NAME', 'text-option-provider')
MESSAGING_HOST = getenv('MESSAGING_HOST', 'localhost')
MESSAGING_PORT = getenv('MESSAGING_PORT', '29092')

# Logging config
LOG_LEVEL = getenv("LOG_LEVEL", "DEBUG")
log = logging.getLogger(APP_NAME)
log.setLevel(logging.DEBUG)
log_console_handler = logging.StreamHandler()
log_console_handler.setLevel(LOG_LEVEL)
log_console_handler.setFormatter(logging.Formatter('%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s'))
log.addHandler(log_console_handler)


####################
# Helper functions
####################

def send_answer_message(payload):
    global producer
    log.debug("Sending answer message to topic %s. Message: %s", MESSAGING_SEND_TOPIC_NAME, payload)
    producer.send(MESSAGING_SEND_TOPIC_NAME, payload)
    producer.flush()


def start_message_consuming(on_message_callback):
    global consumer
    log.info("Starting messages consuming from topic %s",
             MESSAGING_RECEIVE_TOPIC_NAME)
    for message in consumer:
        log.debug("Got message from topic")

        payload = message.value
        log.debug("Message payload: %s", payload)

        on_message_callback(payload)


####################
# Initialization
####################

# Kafka producer
log.info(f"Creating Kafka producer on {MESSAGING_HOST}:{MESSAGING_PORT}")
producer = KafkaProducer(
    bootstrap_servers=[f'{MESSAGING_HOST}:{MESSAGING_PORT}'],
    value_serializer=lambda x: dumps(x).encode('utf-8'))

# Kafka consumer
log.info(f"Creating Kafka consumer on topic {MESSAGING_RECEIVE_TOPIC_NAME} with group_id {GROUP_NAME}")
consumer = KafkaConsumer(MESSAGING_RECEIVE_TOPIC_NAME,
                         bootstrap_servers=[f'{MESSAGING_HOST}:{MESSAGING_PORT}'],
                         group_id=GROUP_NAME,
                         value_deserializer=lambda x: loads(x.decode('utf-8')))


####################
# Main
####################

def handle_message_payload(payload):
    answer = {
        'user_request_id': payload['user_request_id'],
        'request_text': payload['user_request_text']
    }

    send_answer_message(answer)
    log.debug("Answer message was sent")


if __name__ == '__main__':
    p = Process(target=start_message_consuming, args=(handle_message_payload,))
    p.start()
