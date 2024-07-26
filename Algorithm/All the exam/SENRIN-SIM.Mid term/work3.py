text=input()
result=""
sum=0
for i in range(len(text)):
    if text[i]!=" ":
        result=(text[i])
        if text[i]=="10" or text[i]=="12":
            result+=""
        sum+=int(result)
    elif text[i]==" ":
        result=result
if sum == 20:
    print("WON")
else:
    print("LOST")



