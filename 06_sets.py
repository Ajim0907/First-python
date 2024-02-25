#sets are unorederd and only unique values are allowed
days = {'sun', 'mon', 'tue', 'wed', 'fri', 'sat','mon'}
print(days)

#to add value in sets 
days.add('thu')
print(days)

#to change list into sets
list = ["sun", "mon", "wed", "thu", "fri", "sun", "mon"]
print(list)
my_set= set(list)
print(my_set)