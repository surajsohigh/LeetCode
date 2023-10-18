import math 


def factor(n):
    # Write your code here
    li = []
    i=1
    while i <= math.sqrt(n):
        if n % i == 0:
            li.append(i)
            if n // i != i:
                li.append(n // i)
        i += 1

    res=sum(li)
    return res


def sumOfAllDivisors(n: int) -> int:
    res=0
    for i in range(1, n+1):
        res=res+factor(i)
    # print("k",res)
    
    return res
