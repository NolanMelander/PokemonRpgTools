import quantumrandom as qr
import connect as c

def getStats():
    connection = c.connect()
    random = int(qr.randint(1,150))
    db_info = connection.get_server_info()
    cursor = connection.cursor()
    sql = 'Select * from Stats where `National Dex`=%s'
    cursor.execute(sql, (random,))
    rec = cursor.fetchall()

    if connection.is_connected():
        connection.close()

    return rec
