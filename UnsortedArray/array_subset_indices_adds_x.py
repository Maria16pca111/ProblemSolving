
#42. Given an unsorted integer array A and a value X, check if there exists a subset of A of size two that adds upto X and print the indices of the values that adds upto X.
import math
def subset_return_index(a,b,c):
        for x in a:
                a.index(x)
                for y in b:
                        if(x+y==c):
                                b.index(y)
                                print x,y
        return x,y
a=[1,2,3,4,5]
b=[1,2,3]
c=5
subset_return_index(a,b,c)





