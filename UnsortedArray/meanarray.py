def meanArray(x):
    sum1=0
    count=0
    mean=0
    for i in x:
        sum1+=i
        count+=1
        mean=sum1/count
    return mean
x=[7,9,8]
print(meanArray(x))