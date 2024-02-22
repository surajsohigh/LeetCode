from os import *
from sys import *
from collections import *
from math import *

n = int(input())
siz = len(str(n))
tot=0
q=n
while q>0:
    r=q%10
    tot=tot+(r**siz)
    q=q//10

    # print(r,tot, )



if tot==n:
    print("true")
else:
    print("false")


