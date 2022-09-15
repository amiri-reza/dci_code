import datetime

print("------------Task 1-----------------")


current_datetime = datetime.date.today()
print(current_datetime.year)

print("------------Task 2-----------------")

some_date = datetime.date.today()
print(some_date.weekday())

print("------------Task 3-----------------")

this_year = datetime.date.today().year
if (this_year % 400 == 0) or (this_year % 100 != 0) and (this_year % 4 == 0):
    print(f"{this_year} is a leap year.")
else:
    print(f"{this_year} is not a leap year.")

print("------------Task 4-----------------")

date_as_string = "Feb 14 2021 8:30AM"

print(datetime.datetime.strptime(date_as_string, "%b %d %Y %H:%M%p"))





