# def average(time):
#   result=""
#   i=0
#   sumscore=0
#   while i < time:
#     nameStudent=nameStudent
#     score=score
#     for s in range(len(score)):
#       sumscore+=score[s]
#     sumscore/=len(score)
#     result+=("Averrage of",nameStudent,"=",sumscore)+"\n"
#     return result
      





time=int(input("enter:"))
result=""
i=0
sumscore=0
while i < time:
    nameStudent=(input("name:"))
    score=eval(input(".."))
    for s in range(len(score)):
      sumscore+= int(score[s])
    sumscore/=len(score)
    result+=nameStudent, "averrage is",str(sumscore)
    i+=1
print(result)
    