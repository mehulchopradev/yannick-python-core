from db.dbconnect import connect
import json

authorlist = []

def batchinsert():
    try:
        con = connect()
        query = 'insert into authors(name,gender,ratings) values(%s,%s,%s)'
        cursor = con.cursor()

        cursor.executemany(query, authorlist)
    finally:
        if con:
            con.commit()
            con.close()

def addauthortemp():
    name = input('enter author name: ')
    gender = input('enter gender: ')
    ratings = int(input('enter ratings: '))

    authorlist.append((name, gender, ratings))

def verifyandadd():
    for author in authorlist:
        print('Name: {0}\nGender: {1}\nRatings: {2}'.format(author[0], author[1], author[2]))

    choice = input('confirm the above (y/n): ')
    if choice == 'y':
        try:
            batchinsert()
        except Exception:
            print('Unable to add records to db')
        else:
            print('All authors flushed to the database!')
            authorlist.clear()
    else:
        authorlist.clear()

def viewpermanentauthors():
    try:
        con = connect()
    except Exception:
        print('Unable to get the permanent authors. Try again later')
    else:
        cursor = con.cursor()
        query = 'select * from authors where gender = "m"'

        cursor.execute(query)

        for row in cursor:
            print('Name: {0}\nGender: {1}\nRatings: {2}'.format(row[1], row[2], row[3]))

def updatepermanentauthordata():
    '''authorid = int(input('enter id of the author whose data you want to update: '))
    name = input('enter author name: ')
    gender = input('enter gender: ')
    ratings = int(input('enter ratings: '))'''

    with open('authors.json', mode='r') as fp:
        data = json.load(fp)

    datalist = [(d['name'],d['gender'],d['ratings'],d['id']) for d in data]

    try:
        con = connect()
    except Exception:
        print('Unable to get the permanent authors. Try again later')
    else:
        cursor = con.cursor()
        query = 'update authors set name=%s, gender=%s, ratings=%s where id = %s'

        cursor.executemany(query, datalist)
    finally:
        if con:
            con.commit()
            con.close()

def deleteauthor():
    authorid = int(input('enter id of the author whose data you want to update: '))

    try:
        con = connect()
    except Exception:
        print('Unable to get the permanent authors. Try again later')
    else:
        cursor = con.cursor()
        query = 'delete from authors where id = %s'

        cursor.execute(query, (authorid,))
    finally:
        if con:
            con.commit()
            con.close()

while True:
    print('1. Add an author temporarily')
    print('2. Verify and add permanently')
    print('3. View permanently added authors')
    print('4. Update permanent author data')
    print('5. Delete permanent author')
    print('6. Exit')
    choice = int(input('enter choice: '))

    if choice == 1:
        addauthortemp()
    elif choice == 2:
        verifyandadd()
    elif choice == 3:
        viewpermanentauthors()
    elif choice == 4:
        updatepermanentauthordata()
    elif choice == 5:
        deleteauthor()
    else:
        break
