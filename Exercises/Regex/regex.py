import email
import re

text = """Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 

therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com

Kind regards,
Tanisha"""

pattern = r"\w.+@.*[.].*"   # searches for any word plus @ sign plus "." plus everything after "."
emailAdds = re.findall(pattern, text)
print(emailAdds)




pattern2 = r"\w.+@"
usernames = re.findall(pattern2, text)
print(usernames)
# as emailAdds is a list of emails
# for splitting email addresses to username and domain name
# we use 'for loop'
#splitted_username_domain = re.split("@", emailAdds)

for splitted in emailAdds


# for printing each item in the list, we will use 'for loop'
         # split the email addresses according to @ sign

