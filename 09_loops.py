#loops - excute the block of code each time in the sequance
for i in 1,2,3,4,5:
    print(i)

#other ways to write foor loop
    user_list = ["david","paul","robert","tony","carlsen"]
    for user in user_list:
        print(user)

#apply for-loop on dictionary
    student= {
    "hindi": 90,
    "english": 86,
    "maths": 87,
    "history": 89,
    "science": 67
}
for key, value in student.items():
            print("subject is",key)
            print("marks is",value)
            
            
    