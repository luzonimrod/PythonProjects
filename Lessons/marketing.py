print("Hello and welcome to Marketing !\n")
print("This is the Prices: \n Tomatoes = 3 NIS\n Cucumber = 2 NIS\n Coke = 5 NIS\n Chicken = 20 NIS per KG\n")
print("Enter how many Items You Buy\n")
Tomatoes = input("How many Tomatoes did you buy?")
Cucumber = input("How many Cucumber did you buy?")
Coke = input("How many Coke did you buy?")
Chicken = input("How many KG Chickens did you buy?")

Tomatoes = int(Tomatoes)*3
Cucumber = int(Cucumber)*2
Coke = int(Coke)*5
Chicken = int(Chicken)*20
Tax =(float(Tomatoes+Cucumber+Coke+Chicken))*0.17
Total=float(Tomatoes+Cucumber+Coke+Chicken)+Tax
print("Total Amount is:" + str(Total))
