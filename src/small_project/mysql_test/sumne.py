import mysql.connector 
import sys
from pathlib import Path

# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Now import your module
from config import mysqlConfig

try:
    conn = mysql.connector.connect(**mysqlConfig())

    if conn.is_connected():
        cursor = conn.cursor()

        cursor.execute('select * from items')
        for i in cursor.fetchall():
            print(i)
finally:
    cursor.close()
    conn.close()

