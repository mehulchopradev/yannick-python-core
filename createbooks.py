from db.dbconnect import connect

title = input('enter title: ')
pages = int(input('enter pages: '))
price = float(input('enter price: '))

con = connect()

insertquery = 'insert into books(title,pages,price) values(%s,%s,%s)'

'''for performing any SQL operations with ur database table,
from the connection always get the cursor'''
cursor = con.cursor()

# on cursor we can execute any SQL query
cursor.execute(insertquery, (title, pages, price))

# so that finally things hit the database
con.commit()

con.close()
