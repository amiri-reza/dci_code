def normalize(x):
    if x == "October 22nd":
        print(x.upper())
    elif x.isupper() == True:
        print(f"{x.capitalize()}!")
    else:
        print(f"{x.capitalize()}")
normalize("CAPS LOCK DAY IS OVER")
normalize("Today is not caps lock day.")
normalize("Let us stay calm, no need to panic.")