text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

#text3 = text.index("capital")

if (text.find("capital") != -1):
   print("Capital:", text.index("capital"))
else:
    print("There is no such a word in the sentence.")


