# return the count of values with falls in a given range

def Count_Values_Falls_Range(a):
    flag=False    
    for x in a:
        for y in a:
            if not (x==y):
                flag=True
    return y,flag
a=[1,2,2,1,22,2,3]
print(Count_Values_Falls_Range(a))


