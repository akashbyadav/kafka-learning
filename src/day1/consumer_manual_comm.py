from confluent_kafka import Consumer
from config import base_Config

my_configs = {**base_Config(),'group.id':'121123', 'auto.offset.reset':'earliest',
              'enable.auto.commit':False}

my_cons = Consumer(my_configs)
my_cons.subscribe(['day1_topic'])

try:
    while True:
        message = my_cons.poll(timeout=1.0)

        if message is None:
            continue
        elif message.error() is not None:
            print(f'there is a error caused by {message.error()}')
            continue

        print(f'message has been successfully consumed with {message.key().decode()}\
               as key and {message.value().decode()} as value of it')

        my_cons.commit(asynchronous=True)

except KeyboardInterrupt:
    print('user interrupted the process')

except Exception as e:
    print(f'found an exception {e}')

finally :
    my_cons.commit(asynchronous=False)
    my_cons.close()


    

