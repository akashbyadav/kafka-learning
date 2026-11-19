from confluent_kafka import Producer
from config import baseConfig
import random
import time
import json


def call_back(err,msg):
    if err is not None:
        print(f"we encountered some error {err}")
    else:
        print(f"we successfully delivery this message to topic {msg.topic()} and the message was {msg.key().decode()} , {msg.value().decode()}")

configs_ = {**baseConfig(),'acks':'1','linger.ms':'100'}

my_pr = Producer(configs_)

order = [ int(random.uniform(i-10, i+10)) for i in range(2000,30000)]
users = [f'user_{i}' for i in range(100)]
items = [f'item_{i}' for i in range(10)]
quantity = random.randint(1,20)
timestamp = time.time()

Topic = 'Orders'

if __name__ == '__main__':
    for i in range(100):
        key = random.choice(seq=users)
        value = {"order_id":random.choice(seq=order),"user_id":random.choice(seq=users),
            "items_id":random.choice(seq=items),
            "quantity":quantity,
            "timestamp":timestamp}

        my_pr.produce(topic=Topic,value= json.dumps(value),key= key,on_delivery=call_back)
        my_pr.poll(1.0)
        print('-'*20)
        print('sleeping for 2secs')
        time.sleep(2)
        print('starting again after 2secs')
        print(''*20)

    my_pr.flush()
    print('everything has been successfully pushed')