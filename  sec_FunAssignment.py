def countdown(a):
    List_temp=[]
    for x in range(a,-1,-1):
        List_temp.append(x)
    return List_temp


list=countdown(3)
print(list)

def print_and_return (list):
    print(list[0])
    return list[1]

x=print_and_return([1,2])
print(x)

def sumList(a):
    return (a[0]+len(a))

b=sumList([1,2,3,4])
print(b)


def greater_Check(d):
    list=[]
    if len(d)<2:
        return False
    else:
        for x in range(len(d)):
            if d[x]>d[1]:
                list.append(d[x])
            
    print(len(list))
    return list

x=greater_Check([5,2,3,1,4])
print(x)

def length_and_value(size,value):
    temp_list=[]
    for i in range (size):
        temp_list.append(value)
    return temp_list

a=length_and_value(3,4)
print (a)



