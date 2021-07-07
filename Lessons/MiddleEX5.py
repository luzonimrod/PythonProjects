#Write a Python program to find whether a given number (accept from
#the user) is even or odd, print out an appropriate message to the user.

num=input("Enter a number to find if the number is odd or even:")
num2=int(num)
if(num2 % 2 ==0):
    print("The number is even\n")
else:
    print("The number is odd\n")