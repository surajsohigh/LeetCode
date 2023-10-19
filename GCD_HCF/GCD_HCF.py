def calcGDC(n: int, m: int) -> int:

    num1=n
    num2=m

    while num1>0 and num2>0:
        maxi = max(num1, num2)
        mini = min(num1, num2)
 
        res = maxi%mini

        num1=res
        num2=mini

    return max(num2, num1)

