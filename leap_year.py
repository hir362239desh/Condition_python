year = int(input(' enter the number : '))
if year % 400 == 0 or (year % 4 == 0 and year != 100):
    print("Leap year")
else:
    print("Not a Leap year")
