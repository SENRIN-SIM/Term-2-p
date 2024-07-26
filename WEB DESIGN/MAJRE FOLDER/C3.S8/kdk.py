# print(type("145"))
# print(type(145))
# print(type("145.5"))

# n="12"
# r=float(n)
# print(r)

# a=233.05
# b=float(a)
# print(b)
# print(type(b))
# print(a==b)

# text=""
# for n in range(2):
#     print(n)
#     for m in range(2-n):
#         text=text+"x"
#     text=text+"\n"
#     print(text)

# text=""
# for n in range(2):
#     print(n)
#     for m in range(2-n):
#         text=text+"x"
#     text=text+"\n"
# print(text)

# number=int(input())
# text=""
# for n in range(number):
#     for m in range(number-n):
#         text+="x"
#     text=text+"\n"
# print(text)

# number=int(input())
# for n in range(number):
#     # for m in range(number-n):
#     print("idex of n:",str(n))

# x="senrin"
# for i in range(len(x)):
#     print(i,end=" ")

# n=input("enter")
# e=""
# for i in range(len(n)):
#     e=e+n[-(i+1)]
#     print(e)

# n=int(input("enter"))
# e=1
# for i in range(n):
#     # e-=1
#     e=e+i
# print(e)

# x = 0
# condition1 = x = 4
# condition2 = False
# print(condition1)
# while condition1:
#     print(condition2)
#     x += 1
# condition2 = "True"
# print(condition2)


# text = "True"
# boolean = bool(text)
# string = str(boolean)
# condition1 = string < text
# condition2 = text == boolean
# print(condition1)
# print(condition2)

# nb1 = float(True)
# nb2 = int(False, False)
# print(nb1, nb2)

# number = 5
# status = True
# for i in range(number):
#     if status and number >3:
#         print(True)
#     else:
#         status = False
#     number = number -1

# nb1 = "3"
# for i in range(len(nb1)):
#     print("hello" + True)

# number = 4.5
# integer = int(number)
# text = str(number)
# boolean = bool(number)

number = 5
status = True
for i in range(number):
    if status and number >3:
        print(True)
    else:
        status = False
    number = number -1
