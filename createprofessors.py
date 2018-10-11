from db.dbconnect import connect

name = input('enter name: ')
gender = input('enter gender: ')
noofsubjects = int(input('enter no. of subjects taught: '))
subjects = []

for i in range(1, noofsubjects + 1):
    subject = input('enter subject: ')
    subjects.append(subject)

try:
    con = connect()
except Exception:
    print('Unable to connect to the db')
else:
    cursor = con.cursor()
    query1 = 'insert into professors(name,gender) values(%s, %s)'
    cursor.execute(query1, (name, gender))

    con.commit()

    professorid = cursor.lastrowid

    data = []
    for subject in subjects:
        data.append((subject, professorid))

    query2 = 'insert into professor_subjects(subject, professor_id) values (%s, %s)'
    cursor.executemany(query2, data)
finally:
    con.commit()
    con.close()
