import pzem_004t_functions
import mysql.connector as MySQLdb
import datetime
import requests
import sys

# Initialize
cls = pzem_004t_functions.functions()

if (len(sys.argv) < 1):
    print("Usage: pzem_004t_read_dbwrite.py <port>")
    sys.exit(0)
else:
    port = sys.argv[1]  # Windows -> COM*, Linux -> /dev/ttyUSB*, Mac -> /dev/tty.usb*
print(port)
lvalue = list()
lvalue.append(port)

dt_now = datetime.datetime.now()
lvalue.append(dt_now.strftime('%Y%m%d%H%M%S'))

#access to PZEM-004T
try:
    cls.conn(port)
    cls.read_registers()
    print('voltage [v]: ', cls.voltage)
    lvalue.append(cls.voltage)
    print('current [a]: ', cls.current)
    lvalue.append(cls.current)
    print('power [w]: ', cls.power)  # active power (v * i * power factor)
    lvalue.append(cls.power)
    print('energy [wh]: ', cls.energy)
    lvalue.append(cls.energy)
    print('frequency [hz]: ', cls.frequency)
    lvalue.append(cls.frequency)
    print('power factor []: ', cls.powerfactor)
    lvalue.append(cls.powerfactor)
    print('alarm : ', cls.alarm)
    lvalue.append(cls.alarm)
    cls.close()
except Exception as e:
    lvalue.append(0)
    lvalue.append(0)
    lvalue.append(0)
    lvalue.append(0)
    lvalue.append(0)
    lvalue.append(0)
    lvalue.append(0)
    print(e)
    pass

#Write data to Database
db_unix_socket = ''
db_user = 'epever'
db_passwd = 'epever_control01'
db_host = '192.168.11.16'
db_db = 'epever_control'

if (db_unix_socket != ''):
    conn = MySQLdb.connect(unix_socket=db_unix_socket, user=db_user, passwd=db_passwd, host=db_host,
                           database=db_db)
else:
    conn = MySQLdb.connect(user=db_user, passwd=db_passwd, host=db_host, database=db_db)
cur = conn.cursor()
try:
    sql = "INSERT INTO pzem_results2 VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    print(sql)
    cur.execute(sql, lvalue)
    conn.commit()
except MySQLdb.Error as e:
    print(e)
    pass

conn.close()

