import sys
from tkinter import *

# starting tkinter
root = Tk()    # it is necessary for every kinds of codes

# make a new title
root.title("Personal Calculator")


                                                            # create a new simple text label widget
# myLabel = Label(root, text="simple math calculator")          # 'root' for putting label into the root
                                                                # shoving it onto the screen
# myLabel.pack()                                                # or we can use the myLabel.grid(row=0, column=0) to position our labels.

                                                            # adding a new input blank space
#inputScreen = Entry(root, width=75, bg="#ffffff", fg="black", borderwidth=7)
#inputScreen.pack()


# inputScreen.insert(0, "User Input Screen")                    #this line will print a string inside the inputScreen




#adding a function for button
def addition():
    return
    #secondLabel = Label(root, text="hi" )                  # we can have normal string for 'text' or 
                                                            # even concatenate one string with other variable/function or 
                                                            # other functions inside 'text' or
                                                            # having a variable containing a string
                                                            # inputScreen.get() for getting data from inputScreen
    #secondLabel.pack()

#creating a button
# myButton = Button(root, text="=", padx=15, pady=15, command=addition)     # We can add state=DISABLED to the arguments to disable the button.
                                                        # use padx=50/pady=50 or any number to change the size of the button.
                                                        # we can add the functions (by adding 'command=') inside the button to be run by clicking button.
                                                        # we can color the button and text on the button by 'bg="blue' and fg='white' or hex color codes '#000000'.

# myButton.pack()

number1 = Button(root, text="1", padx=30, pady=30, command=addition)
number2 = Button(root, text="2", padx=30, pady=30, command=addition)
number3 = Button(root, text="3", padx=30, pady=30, command=addition)
number4 = Button(root, text="4", padx=30, pady=30, command=addition)
number5 = Button(root, text="5", padx=30, pady=30, command=addition)
number6 = Button(root, text="6", padx=30, pady=30, command=addition)
number7 = Button(root, text="7", padx=30, pady=30, command=addition)
number8 = Button(root, text="8", padx=30, pady=30, command=addition)
number9 = Button(root, text="9", padx=30, pady=30, command=addition)
number0 = Button(root, text="0", padx=30, pady=30, command=addition)
comma = Button(root, text=chr(44), padx=31, pady=30, command=addition)
number00 = Button(root, text="00", padx=26, pady=30, command=addition)
equal   = Button(root, text="=", padx=30, pady=30, command=addition)
plus    = Button(root, text="+", padx=30, pady=30, command=addition)
minus   = Button(root, text=chr(8722), padx=30, pady=30, command=addition)
multiple = Button(root, text="x", padx=30, pady=30, command=addition)
divide  = Button(root, text=chr(247), padx=30, pady=30, command=addition)


number1.grid(row=1, column=0)
number2.grid(row=1, column=1)
number3.grid(row=1, column=2)
number4.grid(row=2, column=0)
number5.grid(row=2, column=1)
number6.grid(row=2, column=2)
number7.grid(row=3, column=0)
number8.grid(row=3, column=1)
number9.grid(row=3, column=2)
comma.grid(row=4, column=0)
number0.grid(row=4, column=1)
number00.grid(row=4, column=2)
equal.grid(row=5, column=4)
plus.grid(row=1, column=4)
minus.grid(row=2, column=4)
multiple.grid(row=3, column=4)
divide.grid(row=4, column=4)


inputScreen = Entry(root, bg="#ffffff", fg="black", borderwidth=7)
inputScreen.grid(row=0, column=0, columnspan=4)







# create an invert loop
root.mainloop()







num1 = sys.argv[1]
choice = sys.argv[2]
num2 = sys.argv[3]

if choice == "-":
    print(int(num1)-int(num2))
elif choice == "+":
    print(int(num1)+int(num2))











# num1 =      float(input("First number: "))
# num2 =      float(input("Second number: "))
# result =    input("* for 'ADD' press 'A'\n* for 'SUBTRACT' press 'S'\n> ")

# if result.lower() == "a":
#     print(num1 + num2)
# elif result.lower() == "s":
#     print(num1 - num2)
# else:
#     print("enter a valid input!")
