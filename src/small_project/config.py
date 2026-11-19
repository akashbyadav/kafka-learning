from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv())

def baseConfig():
    return {'bootstrap.servers':os.environ['Bootstrap_server'],
            'security.protocol':'SASL_SSL',
            'sasl.mechanisms':'PLAIN',
            'sasl.username':os.environ['API_key'],
            'sasl.password':os.environ['API_secret']}

# def schemaConfig():
#    return {}


def mysqlConfig():
    return {"host":os.environ['host'],
            "port":os.environ['port'],
            'user':os.environ["user"],
            'password':os.environ["password"],
            'database':os.environ["database"]}

if __name__=="__main__":
    output = baseConfig()
    print(output)
    out2 = mysqlConfig()
    print(out2)