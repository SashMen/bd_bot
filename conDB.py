import sqlite3
import config
conn = sqlite3.connect(config.DATABASE)
cur = conn.cursor()
def addrow(message, day):
    bday = (message, day)
    cur.execute("INSERT INTO messages(message, day) VALUES(?, ?);", bday)
    conn.commit()

def checkmessage(message, day):
    cur.execute("SELECT * FROM messages WHERE message = '"+ message +"'")
    res = cur.fetchone()
    if(res and res[1] == message and res[2] == day):
        return True
    return False

def checkday(day):
    cur.execute("SELECT * FROM messages ORDER BY id DESC LIMIT 1")
    res = cur.fetchone()
    if (res and day == res[2]):
        return True
    else:
        return False

def deletedata():
    cur.execute("DELETE FROM messages;")
    cur.execute("DELETE FROM sqlite_sequence WHERE name='messages';")
