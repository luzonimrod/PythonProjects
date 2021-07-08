#Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'

Name=input("Enter two strings and sepreate them with space:")
name2=Name.split(" ")
name3=name2[0]
name4=name2[1]
size=len(name3)
size2=len(name4)
name5=""
name6=""
for i in range(size):
    if(i == 0):
        name5 += name4[0]
    elif(i == 1):
        name5 += name4[1]
    else:
        name5 += name3[i]

for x in range(size2):
    if(x == 0):
        name6 += name3[0]
    elif(x == 1):
        name6 += name3[1]
    else:
        name6 += name4[x]

name7=[]
name7.append(name5)
name7.append(name6)
print(name7)




