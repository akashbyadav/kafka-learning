def call_back(err,msg):
    if err is None:
        print( f"the given {msg} has been successfully delivered \
               to partition - {msg.partition()} and topic - {msg.topic()}")

    else:
        print( f"message {msg} was not delivered because of {err}")