year = int(input("Enter year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            msg = "Leap year."
        else:
            msg = "Not Leap year."
    else:
        msg = "Leap year."
else:
    msg = "Not Leap year."

print(msg)
