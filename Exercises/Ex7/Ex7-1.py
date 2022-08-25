city = "Londen"
print(city)


city = "Berlin"
population = "3645000"

print(city+": "+population)

city = "London"
population = "900000"
print(f"City: {city} ({city.isalpha()})")
print("Population: ", population)

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
find = text.find("capital")
if find != -1:
    print(text.index("capital"))

text = "erlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
print(text.split())

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
print(text.replace("capital", "capital of Germany"))

