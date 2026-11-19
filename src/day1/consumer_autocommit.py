## just a simple demonstration of consumer with string serialization

from confluent_kafka import Consumer
from config import base_Config

consumer_conf = {**base_Config(),"group.id":"1121",
                 'auto.offset.reset':'earliest'}

my_cons = Consumer(consumer_conf) 
my_cons.subscribe(['day1_topic'])
try:
    while True:
        message = my_cons.poll(1.0)
        if message is None:
            continue
        if message.error() :
            print(f"consumer message error {message.error()}")

        print(message.topic(),message.key().decode(),message.value().decode())
        print(f"type of message topic {type(message.topic())}")
        print(f"type of message key {type(message.key())}")
        print(f"type of message value {type(message.value())}")

except KeyboardInterrupt :
    print('user stopping consumer by interrupting')

except Exception as e:
    print(f'the exception was {e}')

finally:
    my_cons.close()