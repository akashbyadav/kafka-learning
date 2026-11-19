from config import base_Config 
from confluent_kafka import Producer
from callback import call_back
import random

producer_conf = {**base_Config(),
    "acks":'all',
    "linger.ms" : 10,
    "compression.type":'snappy'}

my_pr = Producer(producer_conf)

values = ['nanu','avanu','iavnu','yaaru','dboss','nemdi','chitraloka','shitraloka','kfi','oooanna']

i=0
while True:
    my_pr.produce(topic='day1_topic',key=str(random.randint(1,10)) ,
              value= random.choice(seq=values) ,
              on_delivery=call_back)
    my_pr.poll(timeout=1.0)
    i=i+1
    if i==20:
        my_pr.flush()




