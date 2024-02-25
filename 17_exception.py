# your suspicious code always should be in TRY block
#e.g. enter - 0 . below code has zero division error/ 7/0 operation is not valid in python

'''
a = int(input("enter a integer"))
b = 7/a
print()

output will be error and your next code will not be excute

'''
#to avoid this error we should use TRY and EXCEPT block

try:
    a = int(input("enter an integer "))
    b = 7/a 
    print(b)
except:
    print('enter a valid number ')

list = [1,2,3,4,5,6,7]
for i in list:
    print(i)




    

