import sys

currency1 = sys.argv[1]
exchange = sys.argv[2]
dollar2euro = int(currency1)*1.01 
euro2dollar = int(currency1)*0,99


if exchange.lower() == "d":
    print(currency1, "Dollars is equal to ", dollar2euro, "Euros")
elif exchange.lower() == "e":
    print(currency1, "Euros is equal to ", euro2dollar, "Dollars")
else:
    print("Wrong Input!")
