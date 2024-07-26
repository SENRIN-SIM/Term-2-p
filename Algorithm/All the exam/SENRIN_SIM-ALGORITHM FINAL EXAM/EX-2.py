# userWord = ["Meet", "Know", "Week", "See", "Eyes"]
# # userWord = eval(input("Enter word here:"))
# newword = []
# for word in userWord:
#     if "EE" in word or "ee" in word or "Ee" in word:
#         newword.append(word)
# print(newword)


array=['Weekend', 'Eleventh','eled'] 
array1=[]
for i in range(len(array)):
    result=array[i]
    res=""
    for j in range(len(result)-1):
        if result[j].upper()=="E" and result[j+1].upper()=="E":         
            array1.append(array[i])
print(array1)