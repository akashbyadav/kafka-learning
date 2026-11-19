import mysql.connector 
from confluent_kafka import Consumer, Producer
from config import baseConfig, mysqlConfig
import json
import time
from producer import my_pr, call_back

consum_configs = {**baseConfig(),'group.id':'121',
                  'auto.offset.reset':'earliest','enable.auto.commit':'False'}


try:
    my_cons = Consumer(consum_configs)
    conn = mysql.connector.connect(**mysqlConfig())

    if conn.is_connected():
        my_cursor = conn.cursor()
        my_cons.subscribe(['Orders'])

        while True:
            msg = my_cons.poll(1.0)

            if msg is None:
                continue
            elif msg.error() is not None:
                print(f'we have encountered some error {msg.error()}')
                continue
            else:
                # Parse JSON string into a Python dictionary
                value = json.loads(msg.value().decode())
                key = msg.key().decode()
                query = 'select stock_count from items where item_id = %s'
                item_id_here = value['items_id']

                # it requires tuple as an argument
                my_cursor.execute(query,(item_id_here,))

                stock_count = my_cursor.fetchone()[0]
                # Extract integer from tuple (e.g., (50,)

                if stock_count:
                    if stock_count >= value['quantity']:
                        query = 'update items set stock_count = stock_count - %s where item_id = %s'
                        item_id_here = value['items_id']
                        my_cursor.execute(query,(value['quantity'],item_id_here))
                        conn.commit()
                        # Save the stock update to MySQL

                        new_value = {'order_id':value['order_id'],
                             'item_id' : value['items_id'],
                             'status' : 'CONFIRMED',
                              'remaining_stock': stock_count - value['quantity'] }

                        my_pr.produce(topic= 'inventory-events',key = key, value = json.dumps(new_value),on_delivery=call_back)
                        my_pr.poll(1.0)
                    else:
                        
                        new_value = {'order_id':value['order_id'],
                             'item_id' : value['items_id'],
                             'status' : 'OUT_OF_STOCK',
                              'remaining_stock': stock_count }

                        my_pr.produce(topic= 'inventory-events',key = key, value = json.dumps(new_value),on_delivery=call_back)
                        my_pr.poll(1.0)
            my_pr.flush()
            my_cons.commit(asynchronous=True)
            print('-'*20)
            time.sleep(3)
            

except Exception as e:
    print(f'we got an excepetion {e}')

finally:
    my_cons.commit(asynchronous=False)
    my_cursor.close()
    conn.close()
    my_cons.close()

