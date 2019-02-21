import quantumrandom as qr
import connect as c


def getnature():
    connection = c.connect()
    random = int(qr.randint(0, 24))
    cursor = connection.cursor()
    sql = 'Select * from Natures where Nature=%s'
    cursor.execute(sql, (random,))
    rec = cursor.fetchall()

    if connection.is_connected():
        connection.close()

    return rec


def getstats():
    connection = c.connect()
    random = int(qr.randint(1,150))
    cursor = connection.cursor()
    sql = 'Select * from Stats where `National Dex`=%s'
    cursor.execute(sql, (random,))
    rec = cursor.fetchall()

    if connection.is_connected():
        connection.close()

    return rec
