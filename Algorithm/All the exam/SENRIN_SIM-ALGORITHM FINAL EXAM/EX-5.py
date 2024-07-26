# subjectList = eval(input("Enter here:"))
# teacherInformation = eval(input("Enter here:"))
subjectList = [
    {"subject": "html", "class": "WEP-B", "teacher-id": 45},
    {"subject": "algorith", "class": "WEP-A", "teacher-id": 68},
    {"subject": "algorith", "class": "WEP-B", "teacher-id": 39},
    ]
teacherInformation = [
    {"teacher-id": 39, "first-name": "Mengheang", "last-name": "Pho"},
    {"teacher-id": 45, "first-name": "ronan", "last-name": "the best"},
    {"teacher-id": 68, "first-name": "him", "last-name": "Hey"}
    ]
allName = ""
for subLis in subjectList: 
    result = ""
    for teacInfor in teacherInformation:
        getFullName = ""
        if subLis["subject"] == "algorithm":
            if subLis["teacher-id"] == teacInfor["teacher-id"]:
                getFullName = teacInfor["last-name"] +" "+ teacInfor["first-name"]
                allName += getFullName + "\n"
        result = allName
        if result == "":
            result = "No teacher in algorithm subject"  
print(result)







#