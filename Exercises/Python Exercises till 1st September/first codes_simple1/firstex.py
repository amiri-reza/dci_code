emails = ["123whatever@gmail.com","456idontcare@gmail.com","789istilldontmind@hotmail.de","forrealbruvwhatever@gmx.de"]

username1 = emails[0]
username2 = emails[1]
username3 = emails[2]
username4 = emails[3]

username1_split = username1.split("@")[0]
username2_split = username2.split("@")[0]
username3_split = username3.split("@")[0]
username4_split = username4.split("@")[0]


domain1_split = username1.split("@")[1]
domain2_split = username2.split("@")[1]
domain3_split = username3.split("@")[1]
domain4_split = username4.split("@")[1]

print("Usernames: \n" + username1_split, username2_split, username3_split, username4_split)
print("domain names: \n" + domain1_split, domain2_split, domain3_split, domain4_split,)

#usernames = emails[0:4]
#print(usernames)


#email_provider = []

# please fill the two lists with the data from the "emails" list. Use string slicing and methods for extracting what you need
#example:
#  test@mail.com
# usernames = ["test"]
# email_provider = ["mail.com"]
