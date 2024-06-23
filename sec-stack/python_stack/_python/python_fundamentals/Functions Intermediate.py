import random
def randInt (min=None,max=None):
        
        if max!=None and min!=None and max<min:
            max,min = min,max
        num=0
        
        
        if max != None and min==None:
            num = random.random()*max

        elif min!= None and max==None:
            num = random.random()*(100-min)+min

        elif max!=None and min!=None:
            num = random.random()*(max-min)+min

        else:
            num = random.random()*100
        
        return round(num)
    
    
x=randInt(max=2)#between 0-2  (0,1,2)
d=randInt(min=3)#between 3-100 (90)
j=randInt(min=2,max=4)#between 2-4 (2,3,4)
l=randInt(max=3,min=1)#between 1-3    (1,2,3)
print(x,d,j,l)
10
5
5
5
None
3
5
