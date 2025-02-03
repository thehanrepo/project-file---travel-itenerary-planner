import haniaztourtroveadmin
import haniaztourtroveuser
from haniaztourtroveadmin import cur, mycon
import mysql.connector as ms
import pyfiglet
mycon = ms.connect(host="localhost", user="root", password="root1234",database='tourtrove1')

def main():
    print('⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈')
    ascii_text = pyfiglet.figlet_format("WELCOME TO TOUR TROVEZ", font="small")
    print(ascii_text)
    print('⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈')
    print("1.User")
    print("2.Admin")
    print('⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈')
    ch=int(input('Please choose a option from above:'))
    print('⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈︎⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡✈')
    if ch==1:
        haniaztourtroveuser.user()
    elif ch==2:
        print('Enter username and password')
        username=input('Enter username:')
        password=input('Enter password:')
        if username=='tourtrove' and password=='abc123':
            haniaztourtroveadmin.admin()
        else:
            print('Incorrect username and password')
main()            

