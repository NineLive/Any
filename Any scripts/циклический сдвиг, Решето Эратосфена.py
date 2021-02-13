"""Циклический сдвиг влево"""

A = [0,1,2,3,4]
N = 5
tmp = A[0]

for k in range(N-1):
    A[k] = A[k+1]
A[N-1] = tmp
print(A)


"""Циклический сдвиг вправо"""
A = [0,1,2,3,4]
tmp = A[N-1]
for k in range(N-2,-1,-1):
    A[k+1] = A[k]
A[0] = tmp
print(A)



"""Решето Эратосфена"""
N = 200
#A = [x for x in range(N)]
A = [True]*N
A[0] = A[1] = False
for k in range(2,N):
    if A[k]:
        for m in range(2*k, N, k):
            A[m] = False
for k in range(N):
    print(k,'-','простое' if A[k] else 'составное')
input()
