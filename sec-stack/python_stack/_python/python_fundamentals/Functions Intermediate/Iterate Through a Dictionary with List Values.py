def printInfo(some_dict):
    for key ,value in some_dict.items():
        print (len(value) ,key)
        
        for x in value:
            print(x)
        print()
        


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)