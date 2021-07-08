#Write a Python program to count repeated characters in a string.
#Sample string: 'thequickbrownfoxjumpsoverthelazydog'
#Expected output:o4 e3 u2 h2 r2 t2
my_list=["a","b","c","d","e","f","g","h","i","j","k","l",
         "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
size=len(my_list)
counter=""
counter2=0
x=0
size3=0
CountWord = input("Enter a word to know how many characters are repeated:")
size2=len(CountWord)
while True:
    for i in range(size):
        if(CountWord[x] == my_list[i]):
            counter=CountWord[x]
            x+=1
            my_list[i]=""
            break;

    if(x != 0):
        for y in range(size2):
            if(CountWord[y] == counter):
                counter2 += 1

    print(counter + str(counter2))


