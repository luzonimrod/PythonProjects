#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string : 'Net4U'
#Expected output: {'N': 1, 'e': 1, 't': 2, '4': 1, 'U': 1}
Name=input("Enter the string you want convert to dictionary:")
my_dict={}
len=len(Name)
for i in range(len):
    print(Name[i])
    my_dict.update({Name[i] : i})
    print(str(my_dict))

