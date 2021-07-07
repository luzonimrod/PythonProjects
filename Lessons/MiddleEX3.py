#Write a Python program to accept a filename from the user and
#print the extension of that.
#Sample filename : abc.java
#Output : java

FileName=input("Enter filename:")
len= len(FileName)
my_list=[]
my_list=FileName.split(".")
print(my_list[1])


#if ("." in FileName):
