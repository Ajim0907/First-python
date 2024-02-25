#dictionary is mostly use for retrive value 
student = {
    "hindi": 90,
    "english": 86,
    "maths": 87,
    "history": 89,
    "science": 67
}
print(student)

#to retrive a perticular value
print(student["hindi"])

#to add item in dictionary
student["geography"]= 97
print(student)

#to delete values from dictinary
del student["maths"]
print(student)

