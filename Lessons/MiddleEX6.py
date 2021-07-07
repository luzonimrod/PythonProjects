#Write a Python script to add a key to a dictionary. Sample Dictionary :
#{0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

my_dict={0:10,1:20,2:30}
new=input("Inset a key:")
new2=input("Insert a value:")
my_dict.update({int(new):int(new2)})
print("New Dictionary is :" +str(my_dict))


