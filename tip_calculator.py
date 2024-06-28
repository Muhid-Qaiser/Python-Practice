print("Weclome to the tip calculator")
bill = input("What was the total bill? ")
bill = float(bill)

percent = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))

ppl = int(input("How many people to split the bill? "))

# does add an additional 0 at the end of the decimal to make it a 2 point decimal
# payment = round(((bill * (1+(percent/100))) / ppl), 2)

# this adds an additional 0 at the end of the decimal to make it a 2 point decimal
#  and also rounds off the decimal point but also converts it into a string
# payment = ((bill * (1+(percent/100))) / ppl)
# payment = "{:.2f}".format(payment)

# alternative method
payment = "{:.2f}".format((bill * (1+(percent/100))) / ppl)

print(type(payment))

print(f"Each person should pay: ${payment}")
