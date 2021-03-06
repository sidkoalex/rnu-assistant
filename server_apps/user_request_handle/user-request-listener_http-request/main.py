import uuid
from json import dumps
from os import getenv
from random import randint
from bottle import route, run
from kafka import KafkaProducer
import logging


####################
# Configurations
####################

# App config
APP_NAME = getenv("APP_NAME", "user-request-listener_http-request")
APP_PORT = getenv("APP_PORT", 8080)
GROUP_NAME = getenv("GROUP_NAME", "user-request-listener")

# Messaging config
MESSAGING_SEND_TOPIC_NAME = getenv('MESSAGING_SEND_TOPIC_NAME', 'user-request-listener')
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


#########################################
# Helper functions
#########################################

def uid():
    random_int = str(randint(0, 1000)).rjust(4, "0")
    short_uuid = str(uuid.uuid4())[:4]
    return f'{random_int}-{short_uuid}'


def send_answer_message(payload):
    global producer
    log.debug("Sending answer message to topic %s. Message: %s", MESSAGING_SEND_TOPIC_NAME, payload)
    producer.send(MESSAGING_SEND_TOPIC_NAME, payload)
    producer.flush()


####################
# Initialization
####################

# Kafka producer
log.info(f"Creating Kafka producer on {MESSAGING_HOST}:{MESSAGING_PORT}")
producer = KafkaProducer(
    bootstrap_servers=[f'{MESSAGING_HOST}:{MESSAGING_PORT}'],
    value_serializer=lambda x: dumps(x).encode('utf-8'))


#########################################
# REST API
#########################################

@route('/')
def home():
    return "<pre>It works! Use it like /text/hello to send commands.</pre>"


@route('/text/<user_text>')
def get_text(user_text):
    log.debug("Got user text %s", user_text)
    answer = {
        "user_request_id": uid(),
        "user_request_text": user_text
    }
    send_answer_message(answer)
    return answer


#########################################
# Run
#########################################

if __name__ == '__main__':
    log.info(f"Running Web Server on port {APP_PORT}")
    run(host="0.0.0.0", port=APP_PORT)
