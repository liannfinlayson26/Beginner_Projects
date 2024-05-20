#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10,12 or 15? %")
people_bill = input("How many people to split the bill? ")

total_bill_converted = float(total_bill)
percentage_converted = float(percentage)
people_converted = int(people_bill)

percentage_converted_2 = (percentage_converted / 100) + 1

total_count = (total_bill_converted / people_converted) *  percentage_converted_2
total_count_round = (round(total_count, 2))
final_amount = "{:.2f}".format(total_count_round)

print(f"Each person should pay: ${final_amount}")
