print("Menu:")
print("Press 1 to get square result for number")
print("Press 2 to Enter 4 ip's to array")
print("Press 3 to Enter 4 DNS addresses to List")
print("Press 4 to check if string is polyndrom")
a=input("Enter you choice:")
if(a == "1"):
    square=input("Enter number to get the square:")
    square = int(square) ** 3
    print("The result is " + str(square))
elif(a == "2"):
    ip=[]
    ip.append(input("Enter ip #1:"))
    ip.append(input("Enter ip #2:"))
    ip.append(input("Enter ip #3:"))
    ip.append(input("Enter ip #4:"))
    print(ip)
elif(a == "3"):
    dns={}
    dns.update({input("dns #1 :"):input("ip #1 :")})
    dns.update({input("dns #2 :"): input("ip #2 :")})
    dns.update({input("dns #3 :"): input("ip #3 :")})
    dns.update({input("dns #4 :"): input("ip #4 :")})
    print(dns)
elif(a == "4"):
    palindromes=input("Enter word to check if it is palindromes:")
    word = palindromes[::-1]
    if(palindromes == word):
        print("this is palindrome !\n")
    else:
        print("This is not palindrome\n")
else:
    print("please enter a number between 1 and 4\n")




