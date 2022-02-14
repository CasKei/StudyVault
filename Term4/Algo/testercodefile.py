def bub(A):
    for i in range(0, len(A) - 1):
        for j in range(len(A) - 1, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1]=A[j-1], A[j]
    return A


def john(A):
    for i in range(len(A)-1,0,-1):
        for j in range(len(A)-1 , i ,-1):
            #print(A)
            if A[j] > A[j-1]:
                A[j], A[j-1]=A[j-1], A[j]
    return(A)

def bubjohn(A):
    for i in range(len(A)-1,0,-1):
        for j in range(len(A)-1,0,-1):
            if A[j] > A[j-1]:
                A[j], A[j-1]=A[j-1], A[j]
    return A

B= [5,7,4,6]
#print(bub(B))
print(john(B))
print(bubjohn(B))

