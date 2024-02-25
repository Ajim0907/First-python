#to create a list []

users = ["alex","jones","david","michell","robert"]
print(users)


#to add the value at the end of the list
users.append("paul")
print(users)

#to delete the value from the list 
users.remove("alex")
print(users)

#to modify the value from the list jones > Jones
users[0]= "Jones"
print(users)

#to add a value at certain position in list
users.insert(0, "alex")
print(users)

#to delete value by index number
del users[5]
print(users)

#to calculate the length of items in list
print(len(users))

#to sorting a list
users.sort()
print(users)

#to reverse sorting 
users.sort(reverse = True)
print(users)

#to remove the recent item in list and to remove by index no ()
users.pop()
print(users)

#numeric list
marks = [90, 76, 86, 78, 54, 76, 70, 56, 83, 65]
print(marks)

#getting the min marks in list
print(min(marks))

#getting the max marks in list
print(max(marks))

#getting sum of the marks
print(sum(marks))



