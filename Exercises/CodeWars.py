
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
