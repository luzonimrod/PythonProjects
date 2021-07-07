#Write a Python program which accepts the user's first and last name and
# print them in reverse order with a space between them.

FirstName=input("Enter your First Name:")
LastName=input("Enter your Last Name:")
print("Your name in reverse is:\n")
print(LastName[::-1] +" " + FirstName[::-1])

