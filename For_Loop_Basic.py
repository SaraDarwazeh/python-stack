def biggie_size(list):
    for x in range(len(list)):
        if list[x]>0:
            list[x]="big"
    return list

x=biggie_size([-1,-2,3,4,6])
print (x)

def count_positives(a):

    count=0
    for x in range(len(a)):
        if a[x]>=0:
            count+=1
    a[len(a)-1]=count
    return a

x=count_positives([-1,3,-4,55,56,67,66])
print (x)

def sum_total(s):
    sum=0
    
    for i in range(len(s)):
        sum +=s[i]
    
    return sum

def average(s):
    sum=0
    avg=0

    for i in range(len(s)):
        sum +=s[i]
    avg=sum/len(s)
    return avg

a =average([1,2,3,4])
print(a)

def length(a):
    return(len(a))

print (length([1,2,3,4]))
print (length([]))

def max(s):
    if len(s)==0:
            return False
    
    else:
        max=s[0]
        for x in range(1,len(s)):
            if s[x]>max:
                max=s[x]
                continue
        
    return max

print(max([1,2,3,45]))

def min(s):
    if len(s)==0:
            return False
    
    else:
        min=s[0]
        for x in range(1,len(s)):
            if s[x]<min:
                min=s[x]
                continue
        
    return min

print(min([1,2,3,45]))


def ultimate_analysis(d):
    anal={'sumTotal': sum_total(d), 'average': average(d), 'minimum': min(d), 'maximum':max(d), 'length': length(d) }
    return anal

d=ultimate_analysis([1,2,3,4,5])
print(d)

def Reverse_List(a):
    i=1
    for x in range(len(a)):
        temp=a[x]
        a[x]= a[len(a)-(x+i)]
        a[len(a)-(x+i)]=temp
        i+=1
        return a
        
        
a=[1,2,3,4,5]
print(Reverse_List(a))



