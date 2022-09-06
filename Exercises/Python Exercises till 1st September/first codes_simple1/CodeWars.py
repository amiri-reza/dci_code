
# no space ------------------------------------------------------------
def no_space(x):
    x = x.replace(" ", "")
    print(x) 

no_space('reza      amiri')


#mile per galon -------------------------------------------------------
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg *fuel_left:
        return True
    else:
        return False

print(zero_fuel(96, 15, 4))


# find the needle -----------------------------------------------------
def find_needle(haystack):
    if "needle" in haystack:
        print(f"found the needle at position", haystack.index("needle"))

def find_needle(haystack):
    return "found the needle at position {}".format(haystack.index("needle"))

#rock paper scissors --------------------------------------------------
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    else:
        return "Player 2 won!"


# number of sheep in an array ----------------------------------------
'''Consider an array/list of sheep where some sheep may be missing from their 
place. We need a function that counts the number of sheep present in the array
(true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined'''

def count_sheep(sheep):
    return ([1 for s in sheep if s])



sheep = ["sheep", 1, 2, 3, 4,
         "sheep", 1, 3, "sheep", 4,
         4, 3, 2, "sheep", 6,
         4, 23, "hi", "to", "sheep"]

print(count_sheep(sheep))



# increased by former number
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

def summation(num):
    x = 0
    x1 = 1
    plus = 1
    for plus in range(num+1):
        plus = x + plus
        x = plus
    return plus

# clock in milliseconds

Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

def past(h, m, s):
    return h*3600000 + m*60000 + s*1000

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans)

# Take 2 strings s1 and s2 including only letters from a to z. 
# Return a new sorted string, the longest possible, containing distinct letters - 
# each taken only once - coming from s1 or s2.
#a = "xyaabbbccccdefww"
#b = "xxxxyyyyabklmopq"
#longest(a, b) -> "abcdefklmopqwxy"

def longest(s1, s2):
    
    # Defining the Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Concatenating the Two Given Strings
    s = s1 + s2
    
    # Declaring the Output Variable
    y = ""
    
    # Comparing whether a letter is in the string
    for x in alphabet:
      if x not in s:
        continue
      if x in s:
        y = y + x
        
    # returning the final output    
    return y








