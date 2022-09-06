text = """One morning, when Gregor Samsa woke from o l troubled dreams, 
he found himself transformed in his bed into a horrible vermin.
 He lay on his armour-like back, and if he lifted his head a 
little he could see his brown belly, slightly domed and divided by 
arches into stiff sections. The bedding was hardly able to cover 
it and seemed ready to slide off any moment. His many legs, pitifully 
thin compared with the size of the rest of him, waved about helplessly 
as he looked."""


hello = "hello"
result_1 = ""
for character in hello:
    
    while character in text:
        
        character = result_1 + character           
        result_1 = character                  
        break
print(result_1.capitalize(), (text.split())[3])








#hello = "hello"
#if any(x in hello for x in g):
    #print(hello.capitalize(), (g.split())[3])
        



#hello = f"{g[(g.find('h'))]}{g[(g.find('e'))]}{g[(g.find('l'))]}{g[(g.find('l'))]}{g[(g.find('o'))]}"
#print(f"{hello.capitalize()} {(g.split())[3]} ")