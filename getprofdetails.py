from db.dbconnect import connect

professorid = int(input('enter the id of the professor whose details u wanna see: '))

try:
    con = connect()
except Exception:
    print('Unable to connect to the database')
else:
    query = """select * from yannickpythondb.professors a, yannickpythondb.professor_subjects b
            where a.id = b.professor_id
            and a.id = %s;"""
    cursor = con.cursor()

    cursor.execute(query, (professorid,))

    idencountered = -1

    for row in cursor:
        if row[0] != idencountered:
            idencountered = row[0]
            print('Name : {0}'.format(row[1]))
            print('Gender : {0}'.format(row[2]))
            print('Subject : {0}'.format(row[4]))
        else:
            print('Subject: {0}'.format(row[4]))
finally:
    if con:
        con.commit()
        con.close()
