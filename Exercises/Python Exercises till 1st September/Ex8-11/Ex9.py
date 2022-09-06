def normalize(message):
    # if the input is October 22nd, it will be uppercase.
    if message == "October 22nd":
        print(message.upper())
    #  if the message is uppercase, it will be capitalized with "!" mark.
    elif message.isupper() == True:
        print(f"{message.capitalize()}!")
    # if the message is lowercase, it will be just capitalized.
    else:
        print(f"{message.capitalize()}")
normalize("CAPS LOCK DAY IS OVER")
normalize("Today is not caps lock day.")
normalize("Let us stay calm, no need to panic.")
normalize("October 22nd")