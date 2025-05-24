#user input
email = input("enter email: ")

#email separation check
if not email.find("@gmail.com") == -1:
    domain_length = 10
elif not email.find("@hotmail.com") == -1 or not email.find("@outlook.com") ==-1:
    domain_length = 12
else:
    print("email not valid")
    domain_length = len(email)

#email separation

address_length = len(email) - domain_length
email_address = email[0 : address_length]

#output
print(email_address)