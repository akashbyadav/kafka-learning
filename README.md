# day 1 --> Producer, Consumer, Admin Client
# Producer methods

produce, produce_batch, poll, flush, delivery_callback,list_topics(),init_transactions/ begin_transaction/ commit_transaction/abort_transaction(Wraps multi-partition writes in atomic transactions to guarantee exactly-once delivery)


Producer does not send immediately it is asynchronous, produce() -> buffer -> broker

## configurations
#### bootstrap.servers -> 
my server ip
#### retries -> might be related to number of retries  
#### acks-> 
specifies number of broker acknowledgment producer require before considering a request complete
#### enable.idempotence -> 
ensure that retries do not write duplicate to partition when its 'true'
#### batch.size ->
sets a maximum byte size of a record batch sent to a partition
#### linger.ms -> 
adds some delay to enable more records to accumulate in a single batch before sending
#### compression.type -> 
compresses batch using codec like gzip,snappy, to reduce network overhead

# Consumer methods
subscribe, poll, commit, close(graceful_shutdown), seek(moves pointer to specific offset or timestamp), assign(manually binds customer to specific partition bypassing group rebalancing)

** delivery guarantee for a consumer
1. At-most-once -> consume message -> commit -> process
2. At least once -> consume message -> process -> commit
3. Exactly once

## configurations
#### group.id -> 
assigns this consumer to a group
#### auto.offset.reset -> 
read stratergy
#### enable.auto.commit
#### session.timeout.ms 


There are some Topic and Broker properties you can look into it from 
http://kafka.apache.org/documentation.html#topicconfigs
https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html?session_ref=https%3A%2F%2Fdocs.confluent.io%2Fcloud%2Fcurrent%2Foverview.html#pyclient-admin-newtopic


# Message

error, key, value, partition, offset, timestamp

# AdminClient and SchemaRegistryClient

create_topics, list_topics(), create_partitions,describe_confgs(), alter_configs(),

AvroSerializer

#### SerializationContext(topic,MessageField.VALUE) 
that validate Python dictionaries against Confluent Schema Registry and encode them into wire-format bytes before calling producer.produce() 

------------------------------------------------------------------

--> whenever you try to get a data from topic in kafka it will be in serialized format(byte format) (both key and value of the message) you need to deserialize it with appropriate schemas 
because you are pushing the serialized records to kafka

--> flow
### In Producer POV
message -> key, value -> serialization -> produce -> poll() -> flush()

### In Consumer POV
subscribe -> poll() -> key, value -> deserialization -> process -> commit() -> close()


----------------------------------------------------------
New Packages/Modules i learnt about

1. python-dotenv (dotenv --> load_env(), find_env()) (whenever you have credentials and you are working in local env instead of exposing it directly inside a code you can use this to place all credentials inside .env file and add it into .gitignore so you don't commit it)
Then you can write config.py file to access these credentials inside a dictionary

2. mysql-connector-python (mysql.connector)(to connect with my mysql database)
-> first create a connection then create a cursor to make exceutions on the database

3. os (to get the path) (os.environ[])

4. json (to serialize and deserialize json or python dictionary)

5. random, time

6. pathlib (pathlib.path) to find a path of the file or get the my parent file path

7. sys (to get the path and system variables)