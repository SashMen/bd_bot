import sqlite3
import config
conn = sqlite3.connect(config.DATABASE)
cur = conn.cursor()
idx = 1
def addrow(message, day):
    global idx
    bday = (idx, message, day)
    cur.execute("INSERT INTO messages VALUES(?, ?, ?);", bday)
    conn.commit()
    idx = idx + 1

def checkmessage(message, day):
    #cur.execute("SELECT * FROM messages ORDER BY id DESC LIMIT 1")
    cur.execute("SELECT * FROM messages WHERE message = '"+ message +"'")
    res = cur.fetchone()
    if(res and res[1] == message and res[2] == day):
        print(res)
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

def resetidx():
    global idx
    idx = 1
