#Write a Python program to display the current date and time. Sample Output :
#Current date and time :
#14:34:14 2014-07-05

from datetime import date
today=date.today()
ti=today.strftime("%d/%m/%Y %H:%M:%S")
print("current date and time :\n " + ti)
