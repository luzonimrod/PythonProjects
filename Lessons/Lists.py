Info=["Nimrod Luzon",29,"Luzon@gmail.com","0547555555"]
print(Info)
ip=["192.168.1.2","172.200.203.11"]
print("Enter 3 ip's")
ip1=input("ip #1:")
ip.append(ip1)
ip2=input("ip #2:")
ip.append(ip2)
ip3=input("ip #3:")
ip.append(ip3)
print("List with all IP's ")
print(ip)
ip.pop(2)
print ("List Except ip #3")
print(ip)