def iterateDictionary(some_list):
    count=0
    for x in some_list:
        for key,value in x.items():
            print (f"{key} - {value}",end="  ")
            count+=1
            if count <len(x):
                print(" , ", end="")
        count=0
        print()

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 