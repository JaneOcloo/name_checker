name=input("Enter your name here:👻") #takes user name as input
print("Heyaa👋 "+ name)#greets the user
name_length = len(name)#calculates teh number fo characters of the name
print(f"Your name has {name_length} characters!")
if name_length>5:
    print("You're a legend!")
else:
    print("You're cool!")

