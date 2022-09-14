import getopt
import sys
 
# getopt module
argumentList = sys.argv[1:]
options = "hf:"
long_options = ["help", "fast"]


arguments, values = getopt.getopt(argumentList, options, long_options)
    

for currentArgument, currentValue in arguments:

    if currentArgument in ("-h", "--help"):
        print ("For Dollar to Euro Exchange Use 'd'\nFor Euro to Dollar Exchange Use 'e'.")
            
    elif currentArgument in ("-f", "--fast"):
        print ("fast mode enabled")
    else:
        print("slow mode enabled")
            


# # start of program
# currency1 = sys.argv[2]
# exchange = sys.argv[3]
# dollar2euro = int(currency1)*1.01 
# euro2dollar = int(currency1)*0,99


# if exchange.lower() == "d":
#     print(currency1, "Dollars is equal to ", dollar2euro, "Euros")
# elif exchange.lower() == "e":
#     print(currency1, "Euros is equal to ", euro2dollar, "Dollars")
# else:
#     print("Wrong Input!")