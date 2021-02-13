




def count(A):
    """ f - массив в который записывается количество каждой введенной цифры
        N - количество всех цифр
    """
    f = [0]*10
    N = 20
    for i in range(N):
        x = A[i]
        f[x]+= 1
    
    return f
    



def test1 (count_def):
    print("Test #1: ")
    A = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,7,7,8]
    f_test = [0,1,2,3,4,5,2,2,1,0]
    f = count_def(A)
    print("ok" if f == f_test else "Fail")
    


if __name__ == "__main__":
    test1(count)
