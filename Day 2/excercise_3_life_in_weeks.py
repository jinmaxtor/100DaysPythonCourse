limit_years = 90
age = input("What is your current age?\n")

remaining_years = limit_years - int(age)
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")