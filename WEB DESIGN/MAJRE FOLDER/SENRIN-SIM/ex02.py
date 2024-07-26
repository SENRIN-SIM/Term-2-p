def containUpperCase(string):
    valid=False
    count=""
    for i in range(len(string)):
        count+=string[i]
    for c in range(len(count)): 
        if count[c]==count[c].upper():
            valid=True
    return valid

string=eval=input("enter text here:")
valid=containUpperCase(string)
print(valid)