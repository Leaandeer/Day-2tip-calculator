#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
Bill = input("What is the total bill? ")
Tip = input("What percentage tip would you like to give? ")
People = input("How many people to split the bill? ")

#Changing Type Formats
Bill_as_float = float(Bill)
Tip_as_float = float(Tip)
People_as_int = int(People)

#Calculations
Tip_as_percent = Tip_as_float / 100
Total_tip_amount = Bill_as_float * Tip_as_percent
Total_bill = Bill_as_float + Total_tip_amount
Bill_per_person = Total_bill / People_as_int
Total_Per_Person = round(Bill_per_person, 2)
Total_Per_Person = "{:.2f}".format(Bill_per_person)

#print Amount
print(f"Each person should pay: CHF {Total_Per_Person}")

