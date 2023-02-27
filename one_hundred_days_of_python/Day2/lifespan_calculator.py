import time

# # This file returns the amount of weeks someone can
# # live up to based on their current age assuming they live
# until 90

# Assuming: 
# 1 year = 365 days
# 1 year = 52 weeks 
# 1 year = 12 months 

# This function is used to print time-delayed 
# dots to the terminal
def print_dots(numdots = 3):

    dot = '.'
    x = 0
    numdots

    while x < numdots:
        time.sleep(0.4)
        print(dot, end=" ")
        x+=1

# initial welcome to the user
time.sleep(1)
print("\nWelcome!\n\n")
time.sleep(2)
print("Today you will be reminded of your mortatlity!\n\n")
time.sleep(2)
print("It's for the better really", end="")
print_dots(5)

current_age = int(input("how old are you dear? \n"))

time.sleep(2)
print("\nOkay", end=" ")
print_dots(7)
print("oof", end = " ")
print_dots(5)

# Find time a ninetey year old lives 

DAYS_90 = 90*365
WEEKS_90 = 90*52
MONTHS_90 = 90*12

est_time_days = DAYS_90 - current_age*365 
est_time_weeks = WEEKS_90 - current_age*52
est_time_months = MONTHS_90 - current_age*12

print(f"""\n\nYou have {est_time_days} days, {est_time_weeks} weeks, 
and {est_time_months} months left in samsara.""")