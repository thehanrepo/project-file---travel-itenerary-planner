#TRAVEL ITINERARY PLANNER - ADMIN
import mysql.connector as ms
from prettytable import from_db_cursor as p
from prettytable import PrettyTable
mycon = ms.connect(host="localhost", user="root", password="root1234")
if mycon.is_connected():
    print('Successfully executed')    
cur = mycon.cursor()
print(cur)
cur.execute("CREATE DATABASE IF NOT EXISTS tourtrove1")
cur.execute("USE tourtrove1")


# DESTINATION TABLES
cur.execute("""
    CREATE TABLE IF NOT EXISTS DESTINATION(
        destination_id INT PRIMARY KEY,
        destination_name VARCHAR(255) NOT NULL,
        description VARCHAR(255) NOT NULL)""")

def insertd():
    print('====================================================================')
    print('Inserting details')
    print('====================================================================')
    while True:
        did = int(input("Enter destination id:"))
        dname = input('Enter destination name:')
        description = input('Enter description:')
        
        query = "INSERT INTO DESTINATION VALUES ({},'{}','{}')".format(did, dname, description)
        cur.execute(query)
        mycon.commit()
        
        print('==================================================================')
        ch = input("More data? (y/n):")
        if ch.lower() == 'n':
            break

def deleted():
    print('====================================================================')
    print('Deleting Details')
    print('====================================================================')
    did_to_delete = int(input('Enter destination id to be deleted:'))
    delete_query = "DELETE FROM DESTINATION WHERE destination_id = {}".format(did_to_delete)
    cur.execute(delete_query)
    mycon.commit()
    print('Record deleted')

def updated():
    print('====================================================================')
    print('Updating Details')
    print('====================================================================')
    print('What would you like to update? ')
    print('1. Destination name ')
    print('2. Description')
    print('3. Exit')
    
    while True:
        choice = int(input('Enter choice:'))
        print('==================================================================')
        
        if choice == 1:
            x = input('Enter new destination name:')
            y = int(input('Enter destination id:'))
            query = "UPDATE DESTINATION SET destination_name='{}' WHERE destination_id={}".format(x,y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 2:
            x = input('Enter new description: ')
            y = int(input('Enter destination id:'))
            query = "UPDATE DESTINATION SET description='{}' WHERE destination_id={}".format(x,y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 3:
            break
        else:
            print('Enter a valid choice.')

def searchd():
    print('====================================================================')
    print('Searching Details')
    print('====================================================================')
    x = int(input("Enter destination id to search:"))
    query = "SELECT * FROM DESTINATION WHERE destination_id={}".format(x)
    cur.execute(query)
    table = p(cur, max_width=10)
    print(table)

def showd():
    cur.execute('SELECT * FROM DESTINATION')
    result = cur.fetchall()  
    table = PrettyTable()
    table.max_width = 10
    column_names = [desc[0] for desc in cur.description]
    table.field_names = column_names
    for row in result:
        table.add_row(row)
    print(table)

def destination():
    while True:
        print('=================================================================')
        print('DESTINATION DETAILS')
        print('=================================================================')
        print('Choose from options below')
        print('1. Insert details')
        print('2. Delete Details')
        print('3. Update Details')
        print('4. Search Details')
        print('5. All records')
        print('6. Exit')
        print('=================================================================')

        ch = int(input('Enter choice:'))
        print('=================================================================')

        if ch == 1:
            insertd()
        elif ch == 2:
            deleted()
        elif ch == 3:
            updated()
        elif ch == 4:
            searchd()
        elif ch == 5:
            showd()
        elif ch == 6:
            break
        else:
            print('Please enter a valid choice.')

# TRIP PACKAGES TABLE
cur.execute("""
    CREATE TABLE IF NOT EXISTS TRIPPACKAGES(
        trip_id INT PRIMARY KEY,
        trip_name VARCHAR(255) NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        budget INT NOT NULL)""")

def insertt():
    print('====================================================================')
    print('Inserting Trip Information')
    print('====================================================================')
    while True:
        tid = int(input("Enter trip id:"))
        tname = input('Enter trip name:')
        startd = input('Enter start date (YYYY-MM-DD):')
        endd = input('Enter end date (YYYY-MM-DD):')
        budget = int(input('Enter budget:'))        
        query = "INSERT INTO TRIPPACKAGES (trip_id, trip_name, start_date, end_date, budget) VALUES ({}, '{}', '{}', '{}', {})".format(tid, tname, startd, endd, budget)
        cur.execute(query)
        mycon.commit()
        print('====================================================================')
        ch = input("More data? (y/n):")
        if ch.lower() == 'n':
            break

def deletet():
    print('====================================================================')
    print('Deleting Trip Information')
    print('====================================================================')
    x = int(input('Enter trip id to be deleted:'))
    query = "DELETE FROM TRIPPACKAGES WHERE trip_id = {}".format(x)
    cur.execute(query)
    mycon.commit()
    print('Record deleted')

def updatet():
    print('====================================================================')
    print('Updating Trip Information')
    print('====================================================================')
    print('What would you like to update? ')
    print('1. Trip name ')
    print('2. Start date')
    print('3. End date')
    print('4. Budget')
    print('5. Exit')
    
    while True:
        choice = int(input('Enter choice:'))
        print('====================================================================')
        if choice == 1:
            x = input('Enter new trip name:')
            y = int(input('Enter trip id:'))
            query = "UPDATE TRIPPACKAGES SET trip_name='{}' WHERE trip_id={}".format(x,y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 2:
            x = input('Enter new start date (YYYY-MM-DD): ')
            y = int(input('Enter trip id:'))
            query = "UPDATE TRIPPACKAGES SET start_date='{}' WHERE trip_id={}".format(x,y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 3:
            x = input('Enter new end date (YYYY-MM-DD): ')
            y = int(input('Enter trip id:'))
            query = "UPDATE TRIPPACKAGES SET end_date='{}' WHERE trip_id={}".format(x,y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 4:
            x = float(input('Enter new budget: '))
            y = int(input('Enter trip id:'))
            query = "UPDATE TRIPPACKAGES SET budget={} WHERE trip_id={}".format(x,y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 5:
            break
        else:
            print('Enter a valid choice.')

def searcht():
    print('====================================================================')
    print('Searching Trip Information')
    print('====================================================================')
    x = int(input("Enter trip id to search:"))
    query = "SELECT * FROM TRIPPACKAGES WHERE trip_id={}".format(x)
    cur.execute(query)
    table = PrettyTable()
    table.field_names = [desc[0] for desc in cur.description]
    for row in cur.fetchall():
        table.add_row(row)
    print(table)

def showt():
    cur.execute('SELECT * FROM TRIPPACKAGES')
    result = cur.fetchall()  
    table = PrettyTable()
    table.max_width = 10
    column_names = [desc[0] for desc in cur.description]
    table.field_names = column_names
    for row in result:
        table.add_row(row)
    print(table)

def trippackage():
    while True:
        print('====================================================================')
        print('TRIP PACKAGES')
        print('====================================================================')
        print('Choose from options below')
        print('1. Insert details')
        print('2. Delete delete')
        print('3. Update details')
        print('4. Search details')
        print('5. Show details')
        print('6. Exit')
        print('====================================================================')
        
        ch = int(input('enter choice: '))
        print('====================================================================')
        if ch == 1:
            insertt()
        elif ch == 2:
            deletet()
        elif ch == 3:
            updatet()
        elif ch == 4:
            searcht()
        elif ch == 5:
            showt()
        elif ch == 6:
            break
        else:
            print('Please enter a valid choice.')

# HOTELS TABLE
cur.execute("""
    CREATE TABLE IF NOT EXISTS HOTELS(
        hotel_id INT PRIMARY KEY,
        hotel_name VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL,
        price_per_night INT NOT NULL,
        deals VARCHAR(255))""")

def inserth():
    print('====================================================================')
    print('Inserting Hotel Information')
    print('====================================================================')
    while True:
        hid = int(input("Enter hotel id:"))
        hname = input('Enter hotel name:')
        location = input('Enter location:')
        price_per_night = int(input('Enter price per night:'))
        deals=input('enter deals: ')
        query = "INSERT INTO HOTELS (hotel_id, hotel_name, location, price_per_night,deals) VALUES ({}, '{}', '{}', {},'{}')".format(hid, hname, location, price_per_night,deals)
        cur.execute(query)
        mycon.commit()
        print('====================================================================')
        ch = input("More data? (y/n):")
        if ch.lower() == 'n':
            break

def deleteh():
    print('====================================================================')
    print('Deleting Hotel Information')
    print('====================================================================')
    x = int(input('Enter hotel id to be deleted:'))
    query = "DELETE FROM HOTELS WHERE hotel_id = {}".format(x)
    cur.execute(query)
    mycon.commit()
    print('Record deleted')

def updateh():
    print('====================================================================')
    print('Updating Hotel Information')
    print('====================================================================')
    print('What would you like to update? ')
    print('1. Hotel name ')
    print('2. Location')
    print('3. Price per night')
    print('4. Deals')
    print('5. Exit')
    
    while True:
        choice = int(input('Enter choice:'))
        print('====================================================================')
        if choice == 1:
            x = input('Enter new hotel name:')
            y = int(input('Enter hotel id:'))
            query = "UPDATE HOTELS SET hotel_name='{}' WHERE hotel_id={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 2:
            x = input('Enter new location: ')
            y = int(input('Enter hotel id:'))
            query = "UPDATE HOTELS SET location='{}' WHERE hotel_id={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 3:
            x = int(input('Enter new price per night: '))
            y = int(input('Enter hotel id:'))
            query = "UPDATE HOTELS SET price_per_night={} WHERE hotel_id={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 4:
            x = int(input('Enter new deals: '))
            y = int(input('Enter hotel id:'))
            query = "UPDATE HOTELS SET deals={} WHERE hotel_id={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 5:
            break
        else:
            print('Enter a valid choice.')

def searchh():
    print('====================================================================')
    print('Searching Hotel Information')
    print('====================================================================')
    x = int(input("Enter hotel id to search:"))
    query = "SELECT * FROM HOTELS WHERE hotel_id={}".format(x)
    cur.execute(query)
    table = PrettyTable()
    table.field_names = [desc[0] for desc in cur.description]
    for row in cur.fetchall():
        table.add_row(row)
    print(table)

def showh():
    cur.execute('SELECT * FROM HOTELS')
    result = cur.fetchall()  
    table = PrettyTable()
    table.max_width = 10
    column_names = [desc[0] for desc in cur.description]
    table.field_names = column_names
    for row in result:
        table.add_row(row)
    print(table)

def hotels():
    while True:
        print('====================================================================')
        print('HOTELS INFORMATION')
        print('====================================================================')
        print('Choose from options below')
        print('1. Insert details')
        print('2. Delete details')
        print('3. Update details')
        print('4. Search details')
        print('5. Show details')
        print('6. Exit')
        print('====================================================================')
        
        ch = int(input('Enter choice:'))
        print('====================================================================')
        if ch == 1:
            inserth()
        elif ch == 2:
            deleteh()
        elif ch == 3:
            updateh()
        elif ch == 4:
            searchh()
        elif ch == 5:
            showh()
        elif ch == 6:
            break
        else:
            print('Please enter a valid choice.')

#ITINERARY TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS ITINERARY(
        itinerary_id INT PRIMARY KEY,
        country_name VARCHAR(255) NOT NULL,
        duration INT NOT NULL,
        activity_type VARCHAR(255) NOT NULL,
        day_1 VARCHAR(255),
        day_2 VARCHAR(255),
        day_3 VARCHAR(255),
        day_4 VARCHAR(255),
        day_5 VARCHAR(255),
        day_6 VARCHAR(255),
        day_7 VARCHAR(255),
        day_8 VARCHAR(255),
        day_9 VARCHAR(255),
        day_10 VARCHAR(255))""")

def inserti():
    print('====================================================================')
    print('Inserting Itinerary Information')
    print('====================================================================')
    while True:
        itid = int(input("Enter itinerary id:"))
        country_name = input('Enter country name:')
        duration = int(input('Enter duration in days:'))
        activity_type = input('Enter activity type:')
        day_1 = input('Enter activities for day 1:')
        day_2 = input('Enter activities for day 2:')
        day_3 = input('Enter activities for day 3:')
        day_4 = input('Enter activities for day 4:')
        day_5 = input('Enter activities for day 5:')
        day_6 = input('Enter activities for day 6:')
        day_7 = input('Enter activities for day 7:')
        day_8 = input('Enter activities for day 8:')
        day_9 = input('Enter activities for day 9:')
        day_10 = input('Enter activities for day 10:')
        
        query = "INSERT INTO ITINERARY (itinerary_id, country_name, duration, activity_type, day_1, day_2, day_3, day_4, day_5, day_6, day_7, day_8, day_9, day_10) VALUES ({},'{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(itid, trip_id, country_name, duration, activity_type, day_1, day_2, day_3, day_4, day_5, day_6, day_7, day_8, day_9, day_10)
        cur.execute(query)
        mycon.commit()
        
        print('====================================================================')
        ch = input("More data? (y/n):")
        if ch.lower() == 'n':
            break

def deletei():
    print('====================================================================')
    print('Deleting Itinerary Information')
    print('====================================================================')
    x = int(input('Enter itinerary id to be deleted:'))
    query = "DELETE FROM ITINERARY WHERE itinerary_id = {}".format(x)
    cur.execute(query)
    mycon.commit()
    print('Record deleted')

def updatei():
    print('====================================================================')
    print('Updating Itinerary Information')
    print('====================================================================')
    print('What would you like to update? ')
    print('1. Country name ')
    print('2. Duration')
    print('3. Activity type')
    print('4. Activities for each day')
    print('5. Exit')
    
    while True:
        choice = int(input('Enter choice:'))
        print('====================================================================')
        if choice == 1:
            x = input('Enter new country name:')
            y = int(input('Enter itinerary id:'))
            query = "UPDATE ITINERARY SET country_name='{}' WHERE itinerary_id={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 2:
            x = int(input('Enter new duration: '))
            y = int(input('Enter itinerary id:'))
            query = "UPDATE ITINERARY SET duration={} WHERE itinerary_id={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 3:
            x = input('Enter new activity type: ')
            y = int(input('Enter itinerary id:'))
            query = "UPDATE ITINERARY SET activity_type='{}' WHERE itinerary_id={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 4:
            print('Enter activities for each day:')
            x = ['day_1', 'day_2', 'day_3', 'day_4', 'day_5', 'day_6', 'day_7', 'day_8', 'day_9', 'day_10']
            for i in x:
                activity = input(f'Enter activities for {day}: ')
                y = int(input('Enter itinerary id:'))
                query = "UPDATE ITINERARY SET {}='{}' WHERE itinerary_id={}".format(i, activity, y)
                cur.execute(query)
                mycon.commit()
            print('Record updated.')
            
        elif choice == 5:
            break
        else:
            print('Enter a valid choice.')

def searchi():
    print('====================================================================')
    print('Searching Itinerary Information')
    print('====================================================================')
    x = int(input("Enter itinerary id to search:"))
    query = "SELECT * FROM ITINERARY WHERE itinerary_id={}".format(x)
    cur.execute(query)
    table = PrettyTable()
    table.field_names = [desc[0] for desc in cur.description]
    for row in cur.fetchall():
        table.add_row(row)
    print(table)

def showi():
    cur.execute('SELECT * FROM ITINERARY')
    result = cur.fetchall()  
    table = PrettyTable()
    table.max_width = 10
    column_names = [desc[0] for desc in cur.description]
    table.field_names = column_names
    for row in result:
        table.add_row(row)
    print(table)


def itineraries():
    while True:
        print('====================================================================')
        print('ITINERARY INFORMATION')
        print('====================================================================')
        print('Choose from options below')
        print('1. Insert details')
        print('2. Delete details')
        print('3. Update details')
        print('4. Search details')
        print('5. Show details')
        print('6. Exit')
        print('====================================================================')
        
        ch = int(input('Enter choice:'))
        print('====================================================================')

        if ch == 1:
            inserti()
        elif ch == 2:
            deletei()
        elif ch == 3:
            updatei()
        elif ch == 4:
            searchi()
        elif ch == 5:
            showi()
        elif ch == 6:
            break
        else:
            print('Please enter a valid choice.')

cur.execute("""
    CREATE TABLE IF NOT EXISTS BOOKING(
        BookingID INT PRIMARY KEY,
        TravelerName VARCHAR(255) NOT NULL,
        Destination VARCHAR(255) NOT NULL,
        DepartureDate DATE NOT NULL,
        ReturnDate DATE NOT NULL,
        HotelName VARCHAR(255) NOT NULL,
        FlightNumber VARCHAR(20) NOT NULL,
        CarRentalCompany VARCHAR(255))
""")


def insertb():
    print('====================================================================')
    print('Inserting Booking Information')
    print('====================================================================')
    while True:
        a = int(input("Enter Booking ID:"))
        b = input('Enter traveler name:')
        c = input('Enter destination:')
        d = input('Enter departure date (YYYY-MM-DD):')
        e = input('Enter return date (YYYY-MM-DD):')
        f = input('Enter hotel name:')
        g = input('Enter flight number:')
        h = input('Enter car rental company:') 
        query = """
            INSERT INTO BOOKING (
                BookingID, 
                TravelerName, 
                Destination, 
                DepartureDate, 
                ReturnDate, 
                HotelName, 
                FlightNumber, 
                CarRentalCompany
            ) VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}')
        """.format(a,b,c,d,e,f,g,h)
        cur.execute(query)
        mycon.commit()
        
        print('====================================================================')
        ch = input("More data? (y/n):")
        if ch.lower() == 'n':
            break

def deleteb():
    print('====================================================================')
    print('Deleting Booking Information')
    print('====================================================================')
    x = int(input('Enter Booking ID to be deleted:'))
    query = "DELETE FROM BOOKING WHERE BookingID = {}".format(x)
    cur.execute(query)
    mycon.commit()
    print('Record deleted')

def updateb():
    print('====================================================================')
    print('Updating Booking Information')
    print('====================================================================')
    print('What would you like to update? ')
    print('1. Traveler name ')
    print('2. Destination')
    print('3. Departure date')
    print('4. Return date')
    print('5. Hotel name')
    print('6. Flight number')
    print('7. Car rental company')
    print('8. Exit')
    
    while True:
        choice = int(input('Enter choice:'))
        print('====================================================================')
        if choice == 1:
            x = input('Enter new traveler name:')
            y = int(input('Enter Booking ID:'))
            query = "UPDATE BOOKING SET TravelerName='{}' WHERE BookingID={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 2:
            x = input('Enter new destination: ')
            y = int(input('Enter Booking ID:'))
            query = "UPDATE BOOKING SET Destination='{}' WHERE BookingID={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 3:
            x = input('Enter new departure date (YYYY-MM-DD): ')
            y = int(input('Enter Booking ID:'))
            query = "UPDATE BOOKING SET DepartureDate='{}' WHERE BookingID={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 4:
            x = input('Enter new return date (YYYY-MM-DD): ')
            y = int(input('Enter Booking ID:'))
            query = "UPDATE BOOKING SET ReturnDate='{}' WHERE BookingID={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 5:
            x = input('Enter new hotel name: ')
            y = int(input('Enter Booking ID:'))
            query = "UPDATE BOOKING SET HotelName='{}' WHERE BookingID={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 6:
            x = input('Enter new flight number: ')
            y = int(input('Enter Booking ID:'))
            query = "UPDATE BOOKING SET FlightNumber='{}' WHERE BookingID={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 7:
            x = input('Enter new car rental company: ')
            y = int(input('Enter Booking ID:'))
            query = "UPDATE BOOKING SET CarRentalCompany='{}' WHERE BookingID={}".format(x, y)
            cur.execute(query)
            mycon.commit()
            print('Record updated.')
            
        elif choice == 8:
            break
        else:
            print('Enter a valid choice.')

def searchb():
    print('====================================================================')
    print('Searching Booking Information')
    print('====================================================================')
    x = int(input("Enter Booking ID to search:"))
    query = "SELECT * FROM BOOKING WHERE BookingID={}".format(x)
    cur.execute(query)
    table = PrettyTable()
    table.field_names = [desc[0] for desc in cur.description]
    for row in cur.fetchall():
        table.add_row(row)
    print(table)

def showb():
    cur.execute('SELECT * FROM BOOKING')
    result = cur.fetchall()  
    table = PrettyTable()
    table.max_width = 10
    column_names = [desc[0] for desc in cur.description]
    table.field_names = column_names
    for row in result:
        table.add_row(row)
    print(table)  

def bookings():
    while True:
        print('====================================================================')
        print('BOOKINGS INFORMATION')
        print('====================================================================')
        print('Choose from options below')
        print('1. Insert details')
        print('2. Delete details')
        print('3. Update details')
        print('4. Search details')
        print('5. Show details')
        print('6. Exit')
        print('====================================================================')
        
        ch = int(input('Enter choice:'))
        print('====================================================================')
        if ch == 1:
            insertb()
        elif ch == 2:
            deleteb()
        elif ch == 3:
            updateb()
        elif ch == 4:
            searchb()
        elif ch == 5:
            showb()
        elif ch == 6:
            break
        else:
            print('Please enter a valid choice.')

            
def admin():
    while True:
        print('⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆')
        print('WELCOME TO ADMIN')
        print('Choose from options below')
        print('⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆')
        print('1. DESTINATION DETAILS')
        print('2. TRIP PACKAGES DETAILS')
        print('3. HOTEL/ACCOMODATION DETAILS')
        print('4. ITINERARY DETAILS')
        print('5. BOOKING DETAILS')
        print('6. EXIT')
        print('⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆')
        ch=int(input('Enter choice:'))
        print('⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆')
        if ch==1:
            destination()
        elif ch==2:
            trippackage()
        elif ch==3:
            hotels()
        elif ch==4:
            itineraries()
        elif ch==5:
            bookings()
        elif ch==6:
            break
        else:
            print('Invalid choice')

