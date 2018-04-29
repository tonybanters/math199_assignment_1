import random
import timeit
import math
import decimal

def mincost(m,n):
    grid = [[random.randint(0,1) for i in range(n)] for j in range(m)]
    T = [[0 for i in range(n)] for j in range (m)]
    T[0][0] = grid [0][0]
    for i in range (1,n):
        T [0][i] = T[0][i-1]+grid [0][i]
    for i in range (1,m):
        T [i][0] = T[i-1][0]+grid [i][0]
    for i in range (1,m):
        for j in range (1,n):
            T[i][j] = grid[i][j]+min(T[i-1][j],T[i][j-1])
    return T[m-1][n-1]


print()
print()
print("---Part(a)---")
print()
print()

print("The average value of the entries in the minimum cost path for a 5x5 grid is: ",
      (mincost(5,5)/(2.0*(5-1))))
print()
print("The average value of the entries in the minimum cost path for a 10x10 grid is: ",
      (mincost(10,10)/(2.0*(10-1))))
print()
print("The average value of the entries in the minimum cost path for a 50x50 grid is: ",
      (mincost(50,50)/(2.0*(50-1))))
print()
print("The average value of the entries in the minimum cost path for a 100x100 grid is: ",
      (mincost(100,100)/(2.0*(100-1))))
print()

print()
print()
print("---Part(b)---")
print()
print()




print("It took ",timeit.timeit("mincost(2500,2500)",
                               "from __main__ import mincost", number = 1),
      "seconds to calculate mincost(2500,2500)." )


def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def scientific_notation(v): # Note that v should be a string for eval()
        d = decimal.Decimal(eval(v))
        e = format(d, '.6e')
        a = e.split('e')
        b = a[0].replace('0','')
        return b + 'e' + a[1]


print()
print()
print("---Part(c)---")
print()
print()

galois = scientific_notation('nCr(4998,2499)')

print("The value for m+n-2 choose m-1 for our mincost(2500,2500) example is: ", galois)
