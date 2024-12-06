# Employee bonus calculation

# Take user input
years_of_service = int(input("Enter years of service: "))
performance_rating = float(input("Enter performance rating (1.0 to 5.0): "))

# Determine bonus percentage
if performance_rating >= 4.5:
    if years_of_service > 10:
        bonus_percentage = 25
    elif years_of_service > 5:
        bonus_percentage = 20
    else:
        bonus_percentage = 15

elif performance_rating >= 3.5:
    if years_of_service > 10:
        bonus_percentage = 20
    elif years_of_service > 5:
        bonus_percentage = 15
    else:
        bonus_percentage = 10

elif performance_rating >= 2.5:
    if years_of_service > 10:
        bonus_percentage = 15
    elif years_of_service > 5:
        bonus_percentage = 10
    else:
        bonus_percentage = 5
else:
    bonus_percentage = 0

# Calculate bonus amount
salary = float(input("Enter current salary: "))
bonus_amount = salary * bonus_percentage / 100

print("Bonus Amount: ", bonus_amount)
