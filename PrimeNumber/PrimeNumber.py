import math 

## Read input as specified in the question.
## Print output as specified in the question.
def isPrime(n):
    i=1
    count=0
    while i<=math.sqrt(n):
        if n%i == 0:
            count = count+1
            if (n//i) != i:
                count = count+1

        i=i+1

    if count == 2:
        print("YES")
    else:
        print("NO")


n = int(input())
isPrime(n)
