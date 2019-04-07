n=input('number')
data=[1,2,3,4,5]
for x in data:
    if not(n==x):
        data.append(n)
        print('yes! you are Inside')
        
    else:
        data.pop(n)
        print('You are out')
print(data)
    