'''
simple login system
'''
'''
usernames=['Ahmed','Ali','Amr']
passwds=  [1394,6078,9345]

name=input("please enter youe user name: ")

if name in usernames:
    passwd=int(input("please input your password: "))
    if passwd == passwds[usernames.index(name)]:
        print(f"Welcome {name}")
    else:
        print("Password is incorrect")
else:
    print("user name is incorrect")    
'''
#-----------------------------------------------

database={'Ahmed':1394 , 'Ali':6078 , 'Amr':9345 }

name=input("please enter youe user name: ")

if name in database:
    passwd=int(input("please input your password: "))
    if passwd == database[name]:
        print(f"Welcome {name}")
    else:
        print("Password is incorrect")
else:
    print("user name is incorrect")