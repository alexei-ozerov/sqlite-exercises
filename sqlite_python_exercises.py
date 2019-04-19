import os
import sqlite3

# Check To See If Database Exists
if os.path.isfile('./sqlite_exercises.sqlite') == False:

    # Database Object
    conn = sqlite3.connect('./sqlite_exercises.sqlite')

    # Cursor Creation
    cursor = conn.cursor()

    # Configure Database
    cursor.execute('create table exercise_logs (id integer primary key autoincrement, type text, minutes integer, calories integer, heart_rate integer);')

    cursor.close()

    # Commit & Close
    conn.commit()
    conn.close()

conn = sqlite3.connect('./sqlite_exercises.sqlite')
cursor = conn.cursor()

def insertLog(t,m,c,h,cursor):
    sql = 'insert into exercise_logs(type, minutes, calories, heart_rate) values (?,?,?,?)'
    cursor.execute(sql, (str(t), int(m), int(c), int(h)))

etype = 'running'
minutes = 60
calories = 200
heart_rate = 80

insertLog(etype, minutes, calories, heart_rate, cursor)
