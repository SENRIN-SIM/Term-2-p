name=eval(input())
result=0
for i in range(len(name)):
    for c in range(len(name[i])):
        if (name[i])[c]=="a":
            result+=1
    print("Number of A in",name[i],"is",result)
    result=0