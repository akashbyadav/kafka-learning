import mysql.connector
from mysql.connector import Error
from config import mysqlConfig

try:
    conn = mysql.connector.connect(**mysqlConfig())

    if conn.is_connected():
        cursor = conn.cursor()

        insert_query = "INSERT INTO items(item_id, stock_count) values (%s,%s)"
        cursor.execute(insert_query,(121,20000))

        conn.commit()

        cursor.execute("SELECT * FROM items limit 5")
        for row in cursor.fetchall():
            print(row)


except Exception as e:
    print(f"some exception has occured {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()