import quantumrandom as qr
import connect as c


def getrows():
    connection = c.connect()
    cursor = connection.cursor()
    sql = 'Select * from Stats'
    cursor.execute(sql)
    cursor.fetchall()
    rows = cursor.rowcount

    if connection.is_connected():
        connection.close()

    return rows


def getnature():
    connection = c.connect()
    random = int(qr.randint(0, 24))
    cursor = connection.cursor()
    sql = 'Select * from Natures where Value=%s'
    cursor.execute(sql, (random,))
    rec = cursor.fetchall()

    if connection.is_connected():
        connection.close()

    return rec


def getstats():
    rows = getrows()
    connection = c.connect()
    random = int(qr.randint(1, rows))
    cursor = connection.cursor()
    sql = 'Select * from Stats where `National Dex`=%s'
    cursor.execute(sql, (random,))
    rec = cursor.fetchall()

    if connection.is_connected():
        connection.close()

    return rec

