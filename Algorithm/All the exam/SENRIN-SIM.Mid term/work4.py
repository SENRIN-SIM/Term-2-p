number=int(input("Enter number:"))
i=0
while number!=68 and i <2:
    number=int(input("Enter number again:"))
    i+=1
    if i == 2 and number!= 68:
        print("YOU LOST!")
if number==68:
    print("YOU WON!")