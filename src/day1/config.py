import os
from dotenv import load_dotenv,find_dotenv


load_dotenv(find_dotenv())

def base_Config():
    return {
        'bootstrap.servers':os.environ['Bootstrap_server'],
        'security.protocol':'SASL_SSL',
        'sasl.mechanisms':'PLAIN',
        'sasl.username':os.environ["API_key"],
        'sasl.password':os.environ['API_secret']
    }

if __name__=="__main__":
    config = base_Config()
    print(config)