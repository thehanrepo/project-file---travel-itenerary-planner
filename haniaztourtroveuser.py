#USER - TOUR TROVEZ
import mysql.connector as ms
from prettytable import from_db_cursor as p
from prettytable import PrettyTable
mycon = ms.connect(host="localhost", user="root", password="root1234", database='tourtrove1')
cur = mycon.cursor()


def book_trippackage():
    print('===============================')
    print('Book your Trip Package!')
    print('===============================')
    while True:
        a = int(input("Enter Trip ID:"))
        b = input('Enter Trip Name:')
        c = input('Enter Start Date (YYYY-MM-DD):')
        d = input('Enter End Date (YYYY-MM-DD):')
        e = int(input('Enter Budget:'))
        query = "INSERT INTO TRIPPACKAGES VALUES({}, '{}', '{}', '{}', {})".format(a,b,c,d,e)
        cur.execute(query)
        mycon.commit()

        print('==============================')
        print('Trip Package has been booked!')
        print('Thank You!')
        print('==============================')

        ch = input("Do you want to book more trips?(y/n):")
        if ch.lower() == 'n':
            break

def book_hotel():
    print('==============================')
    print('Book your Hotel!')
    print('==============================')
    while True:
        a = int(input("Enter Hotel ID:"))
        b = input('Enter Hotel Name:')
        c = input('Enter Location:')
        d = int(input('Enter Price per Night:'))
        e = input('Enter Deals:')
        query = "INSERT INTO HOTELS VALUES({}, '{}', '{}', {}, '{}')".format(a,b,c,d,e)
        cur.execute(query)
        mycon.commit()

        print('==============================')
        print('Hotel has been booked!')
        print('Thank You!')
        print('==============================')

        ch = input("Do you want to book more hotels?(y/n):")
        if ch.lower() == 'n':
            break

def book_trip():
    print('==============================')
    print('Book your Trip!')
    print('==============================')
    while True:
        a = int(input("Enter Booking ID:"))
        b = input('Enter Traveler Name:')
        c = input('Enter Destination:')
        d = input('Enter Departure Date (YYYY-MM-DD):')
        e = input('Enter Return Date (YYYY-MM-DD):')
        f = input('Enter Hotel Name:')
        g = input('Enter Flight Number:')
        h = input('Enter Car Rental Company:')
        query = "INSERT INTO BOOKING VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(a,b,c,d,e,f,g,h)
        cur.execute(query)
        mycon.commit()

        print('==============================')
        print('Trip has been booked!')
        print('Thank You!')
        print('==============================')

        ch = input("Do you want to book more trips?(y/n):")
        if ch.lower() == 'n':
            break

def user():
    while True:
        print('==============================')
        print('Hello User!')
        print('Please choose from the below options.')
        print('==============================')
        print('1.TO BOOK TRIP PACKAGE')
        print('2.TO BOOK HOTELS')
        print('3.TO BOOK A TRIP')
        print('4.EXIT')
        print('==============================')
        ch=int(input('Enter choice:'))
        print('==============================')
        if ch==1:
            book_trippackage()
        elif ch==2:
            book_hotel()
        elif ch==3:
            book_trip()
        elif ch==4:
            break
        else:
            print('Enter valid choice')
            
    print('Thank You for choosing us!')
    print('==================================')
         

