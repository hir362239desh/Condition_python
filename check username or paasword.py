username = input("Username: ")
password = input("Password: ")

if username == "Hirdesh" and password == "12345":
    print("Access Granted!")
elif username != "Hirdesh" and password == "12345":
    print("Incorrect Username")
elif username == "admin" and password != "12345":
    print("Incorrect Password")
else:
    print("Invalid Credentials")