text=input()
isFoundspace=True
result=0
sum=0
for i in range(len(text)):
    if text[i]!=" ":
        result=(text[i])
        sum+=int(result)
    elif text[i]==" ":
        result=sum
if sum <= 20:
    print("WON")
else:
    print("LOST")
