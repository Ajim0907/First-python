#comparison operaters
#used to compare two operands,returns either true or false
#it is also called ralational operators
'''
1) greater than (>)
2) less than (<)
3) greater than or equal to (>=)
4) less than or equal to (<=)
5) equal to (==)
6) is not equal to (!=)

'''
#logical operaters
#logical operaters are used to combine two conditional operators
'''
list of logical operators
1) logical AND (and)
2) logical OR  (or)
3) logical NOT (not)
'''
#logical NOT operators is the only unary logical opertors 

#AND operators
# it returns the true, if both conditions are TRUE, otherwise it returns false

x = 10
y = 20
z = 30
if x > y and y > z:
    print("x is greater than y and z")
else:
    print("x is not greater than y and z ")
    
#OR operators
#it returns TRUE if one of the condition is TRUE
    x = 10
    y = 90
    z = 50
    if x < y or y < z:
        print("x is less than y")
    else:
        print("y is less than z")
        

#logical NOT
#returns TRUE if the conditional expression returns false, and vice versa.
    x = 10
    y = 20
    z = 30
if not(x > y or x > z):
        print("x is not greater than y and z")
else:
            print("x is greater than z")


    
