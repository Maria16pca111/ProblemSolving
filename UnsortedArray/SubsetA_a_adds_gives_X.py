#integer array A and a value X, check if there exists a subset of A of size two that adds upto X (Subset sum for a pair).

def Subset_Pair_X(A,a,X):
    
    for x in A:
        for y in a:
            if(x+y==X):
                print x,y
    return 0               

A=[1,2,3,4,6,7]
a=[1,2,3,4,5]
X=8
print(Subset_Pair_X(A,a,X))
            