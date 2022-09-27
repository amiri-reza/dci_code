'''Birthday Day Calculator
- takes birthday as input
- prints out years, months, weeks & days since
Event Day Calculator
- takes date as input
- prints out years, months, weeks & days until
Personal Project Datetime!
- use datetime
- surprise us!'''

import datetime

user_input_year = int(input("What is your year of birth? "))                    #takes the user input
user_input_month = int(input("What is your month of birth? "))                  #takes the user input
user_input_day = int(input("What is your day of birth? "))                      #takes the user input


formatted_birthday = datetime.datetime(user_input_year, user_input_month, user_input_day)   # converts the int inputs to datetime object --> 1990 2 15
print("Your birthday is", user_input_day, end="")                                          # output will be: 'Your birthday is 15'
if user_input_day == 1 or user_input_day == 21 or user_input_day == 31:                     # if statement for adding 'st | nd | th' to the end of day
    print("st of ", end="")
elif user_input_day == 2 or user_input_day == 22:
    print("nd of ", end="")
else:
    print("th of ", end="")                                                                 # output will be 'st | nd | th'

full_month = datetime.datetime.strftime(formatted_birthday, "%B %Y")            # takes out the full version of month with full version of year from event_date
print(full_month)                                                               # output will be: 'of February 1990'

today = datetime.datetime.today()

total_time = today - formatted_birthday
total_days = total_time.days              # 11593 

passed_years = total_days//365
#print(passed_years)
remained_days_1 = total_days%365

passed_month = remained_days_1//30
#print(passed_month)
remained_days_2 = remained_days_1%30

passed_week = remained_days_2//7
#print(passed_week)
remained_days_3 = remained_days_2%7

passed_days = remained_days_3
#print(passed_days)
print("We assume every year has 365 days and every month has 30 days:")
print(f"You have spend appr. {passed_years} years, {passed_month} months, {passed_week} weeks and {passed_days} days of your life!")


print("""---------------------------------------------------------------------------------------------------------------------""")


user_input_year2 = int(input("In which year does the event take place? "))          #takes the user input
user_input_month2 = int(input("In which month does the event take place? "))        #takes the user input
user_input_day2 = int(input("In which day does the event take place? "))            #takes the user input


event_date = datetime.datetime(user_input_year2, user_input_month2, user_input_day2)    # converts the int inputs to datetime object --> 1990 2 15
print(f"Event starts at {user_input_day2}", end="")                                     # output will be: 'Event starts at 15'


if user_input_day2 == 1 or user_input_day2 == 21 or user_input_day2 == 31:              # if statement for adding 'st | nd | th' to the end of day
    print("st", end="")
elif user_input_day2 == 2 or user_input_day2 == 22:
    print("nd", end="")
else:
    print("th", end="")                                                         # output will be 'st | nd | th' 

full_month2 = datetime.datetime.strftime(event_date, "of %B %Y")                # takes out the full version of month with full version of year from event_date
print(full_month2, end="\n\n")                                                  # output will be: 'of February 1990'


today = datetime.datetime.today()

total_time = event_date - today                             # subtract the todays date to event date (gives back number of days in timedelta object format)

total_days = total_time.days                                # convert the result to a normal integer

passed_years = total_days//365                              # result will be number of number of years
#print(passed_years)
remained_days_1 = total_days%365                            # result will be remaining of days after dividing days to 365

passed_month = remained_days_1//30                          # divide the remaining days to 30
#print(passed_month)
remained_days_2 = remained_days_1%30                        #  the remaining of the divide

passed_week = remained_days_2//7
#print(passed_week)
remained_days_3 = remained_days_2%7

passed_days = remained_days_3
#print(passed_days)

print("We assume every year has 365 days and every month has 30 days:")
print(f"You have appr. {passed_years} years, {passed_month} months, {passed_week} weeks and {passed_days} days remaining to the event!")













