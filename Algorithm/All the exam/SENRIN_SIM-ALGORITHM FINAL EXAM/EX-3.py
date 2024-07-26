def reversText(words):
    storReverswords = []
    for word in words:
        reverString = ""
        for i in range(len(word)):
            reverString += word[len(word)-i-1]
        storReverswords.append(reverString)
    return storReverswords
reversedwordAgain = []
# words = eval(input("Enter word here:"))
words = ["abc", "123", "456"]
reversedword = reversText(words)
for j in range (len(reversedword)):
    reversedwordAgain.append(reversedword[len(reversedword)-j-1])
print(reversedwordAgain)


