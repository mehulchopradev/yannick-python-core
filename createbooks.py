from db.dbconnect import connect

title = input('enter title: ')
pages = int(input('enter pages: '))
price = float(input('enter price: '))

try:
    con = connect()
except Exception:
    print('unable to connect to the db. Please check settings')
else:
    insertquery = 'insert into books(title,pages,price) values(%s,%s,%s)'

    '''for performing any SQL operations with ur database table,
    from the connection always get the cursor'''
    try:
        cursor = con.cursor()

        # on cursor we can execute any SQL query
        cursor.execute(insertquery, (title, pages, price))
    except Exception:
        print('Unable to store the book record. Please try again later')
    else:
        print('Book saved successfully!')
    finally:
        # so that finally things hit the database
        con.commit()
        con.close()
