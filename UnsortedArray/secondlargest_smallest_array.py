# print the second largest element and second smallest element in array

def Smallest_Array_Second(a,k):
        a.sort()
        count=0
        for x in a:
                
                count+=1
                if(count==k):
                        print(x)
a=[25,4,57,8,12]
k=2
Smallest_Array_Second(a,k)        


