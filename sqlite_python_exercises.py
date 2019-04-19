import os
import sqlite3

if os.path.isfile('./sqlite_exercises.sqlite') == False:

    # Database Object
    conn = sqlite3.connect('./sqlite_exercises.sqlite')

    # Cursor Creation
    cursor = conn.cursor()

    # Configure Database
    cursor.execute('CREATE TABLE exercise_logs(id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, minutes INTEGER, calories INTEGER, heart_rate INTEGER);')
    cursor.close()

    # Commit & Close
    conn.commit()
    conn.close()

# Open Connection
conn = sqlite3.connect('./sqlite_exercises.sqlite')
cursor = conn.cursor()

def insertLog(t,m,c,h,cursor):
    sql = 'INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES(?,?,?,?)'
    cursor.execute(sql, (str(t), int(m), int(c), int(h)))

etype = 'running'
minutes = 61
calories = 200
heart_rate = 80

insertLog(etype, minutes, calories, heart_rate, cursor)

#cursor.execute('''INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES(?,?,?,?)''', (etype, minutes, calories, heart_rate))

conn.commit()
conn.close()

print('Data Inserted.')
