my_dict={"nimrod":100,"idan":200,"ira":300,"Vico":400,"Dorin":500}
print(my_dict)
first=(my_dict["nimrod"])
last=(my_dict["Dorin"])
sum=first+last
print("The sum is "+ str(sum))
my_dict.update({"dudu":sum})
print("There are " +str(len(my_dict)) +" Values")
print("Idan found in the Dictionary?")
print("idan" in my_dict)