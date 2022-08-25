text = "Berlin is a world city of culture, politics, media and science."
print(len(text))



print(text[0], text[-1])



#task 3
print(f"First three characters: {text.upper()[:3]}")

#task 4
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
print(f"B appears: {text.count('B')} times")


#task5

text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
print(text[-10:])


#task6

text = "---Python programming---"
print(text.strip("---"))


#task7
first_name = "Mary"
last_name = "Mat"
print(f"Firstname: {first_name}\nLastname: {last_name}")
