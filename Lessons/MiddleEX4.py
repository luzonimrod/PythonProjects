#Write a Python program that accepts an integer (n) and computes
#the value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615
from time import sleep
Number=input("Enter a Number to calc x+xx+xxx:")
sleep(3)
Number2=int(Number * 2)
Number3=int(Number * 3)
sum=int(Number)+Number2+Number3
print("The Result is " + str(sum))
