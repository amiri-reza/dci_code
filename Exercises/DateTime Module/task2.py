import datetime

print("------------Task 1-----------------")

current_time = datetime.datetime.now()
print("current time:                ", current_time)
current_datetime = current_time - datetime.timedelta(days=15)
print("15 days before current time: ", current_datetime)
formatted_version = current_datetime.strftime("%Y-%m-%d")
print("Formatted version:           ", formatted_version)


print("------------Task 2-----------------")

current_time = datetime.datetime.now()
print("current time:                ", current_time)
current_datetime = current_time + datetime.timedelta(days=7)
print("7 days after current time:   ", current_datetime)
formatted_version = current_datetime.strftime("%Y-%m-%d")
print("Formatted version:           ", formatted_version)



print("------------Task 3-----------------")

start_date = datetime.date(year=2020, month=1, day=25)
formatted_version_2 = start_date.strftime("%d %B, %Y")
print(f"Hello Friedrich, your rent of 300 € is due on {formatted_version_2}.")


