def reverseString(string):
    word=""
    reverseword=""
    for i in range(len(string)):
        word=string[i]
        for w in range(len(word)):
            reverseword+=word[(len(word)-w)-1]
        word=""
    return reverseword

string=["Hi","Hello" ]
reverseword=reverseString(string)
print("Reversestring",string,reverseword)


