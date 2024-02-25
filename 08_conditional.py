#enter the no to check the no is even or odd

num = int(input("enter the number- "))
if num%2 ==0 :
    print("the no is even ")
else:
    print("the number is odd ")

#check a specefic value in list
user=["ajim","ansar","kureshi","faraz"]
if "ajim" in user:
        print("yes the user exist")
else:
        print("user dose not exist")
#elif method
marks = int(input("enter the marks "))
if marks>=90:
              print("grade A")
elif marks>=70:
              print("grade B")
elif marks>=60:
              print("grade C")
else:
              print("failed")
