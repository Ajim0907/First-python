# r = read
# a = append
# w = write
# x = create

f = open("names.txt", 'r')
print(f.read())

# to read the first four charcecters of the file
 #-- you cant print the new file once you read the file,to read new file you have to comment out first print fun
print(f.read(4))

# to read the each line in the file
print(f.readline())
print(f.readline())

# append - creates the file if it doesn't exist

f = open('names.txt','a')
f.write(" ,niel")
f.close()

f = open('names.txt','r')
print(f.read())
f.close()

#write - (overwrite)
f = open("names.txt",'w')
f.write("i deleted all the names from this file")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# create - two ways to create a new file
# 1) opens the file for writing, create a file if it doesen't exist
f = open("new_names.txt", 'w')
f.close()

# 2) creates the specified file, but returns an error if the file already exist
import os 
if not os.path.exists("data.txt"):
    f = open("data.txt", 'x')
f.close()

# delete a file
# avoid an error if it exist
if os.path.exists("data.txt"):
    os.remove("data.txt")
else:
    print("the file you wish to delete does not exists")



