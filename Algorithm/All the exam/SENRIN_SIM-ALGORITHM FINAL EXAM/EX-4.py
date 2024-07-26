# studentList = eval(input("Enter here:"))
studentList = [
        {"name":" dyna"," subject":" Algorithm"," score":10},
        {"name":" sokheang"," subject":" Html"," score":45},
        {"name":" sreynang"," subject":" Algorithm"," score":89},
        {"name":" phanit"," subject":" Algorithm"," score":49},
        ]
count = 0
studtFaild = []
for studentRecode in studentList:
    if studentRecode[" subject"] == " Algorithm":
        if studentRecode[" score"] < 50:
            count +=1
            studtFaild.append(studentRecode["name"])
print("Student faild has:",count)
print("Student faided name:",studtFaild)
