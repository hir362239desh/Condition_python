age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age <= 18:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")