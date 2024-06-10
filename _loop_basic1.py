for x in range(151):
    print(x)# from 0 - 150 

print("------------------")

for x in range(5,1001,5):
    print(x) #from 5-1000 malti of 5

print("------------------")

for x in range(101):

    if x%5==0:
        print("coding")

    elif x%10==0:
        print("coding dojo")

    else:print(x)


print("------------------")

sum=0
for x in range(500001):
    if x % 2 != 0:
        sum = sum +x

print ( "sum =", sum)

print("------------------")

for x in range (2018,0,-4):
    print(x)

print("------------------")

lowNum=2
highNUM=9
mult=3

for x in range(lowNum,highNUM+1):
    if x%mult==0:
        print(x)
        