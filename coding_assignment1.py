import math
import random
import statistics


def quicksort(x):
    return _quicksort(x,0,len(x)-1)



def _quicksort(x: "list", l: int, h: int):
    ''' this function will sort a list quickly
    it will return the number of comparisons made. '''
    count = 0
    if l < h:
        p , count = partition(x,l,h) # setting pivot value
        count += _quicksort(x,l,p-1) # sorting left and right
        count += _quicksort(x,p+1,h) # recursively
    return count



def partition(x: "list", l: int, h: int):
    '''this function will partition the list into two lists
    and a pivot value, and will return the position of the pivot,
    and the number of comparisons'''

    count = 0
    pivot = x[h] # pivot value
    j = (l-1)  # index of first leftmost element
    for i in range(l,h):
        count += 1
        if x[i] <= pivot:
            j += 1 # move index of smaller element to the right
            x[i], x[j] = x[j] , x[i] # put smaller element on left side of pivot

    x[j + 1] , x[h] = x[h] , x[j + 1] # swaps last element with last element of left sublist
    return j + 1 , count # return position of last sorted element, and count number of comparisons

print()
print()
print("---Quicksort---")
print("---Parts (a)(b)---")
print()
print()

countlist1 = []
countlist2 = []
countlist3 = []
countlist4 = []
countlist5 = []
for j in range (10):
    x = []
    for i in range (10):
        x.append(random.randint(1,10))
    count = quicksort(x)
    countlist1.append(count)

    
print("The mean comparisons of experiments with list size n = 10 is", statistics.mean(countlist1))
print("The median comparisons of experiments with list size n = 10 is", statistics.median(countlist1))
print("The quotient of the mean divided by n log n is" , statistics.mean(countlist1) / (10*math.log(10)) )
print("The quotient of the median divided by n log n is" , statistics.median(countlist1) / (10*math.log(10)) )

for j in range (10):
    x = []
    for i in range (100):
        x.append(random.randint(1,100))
    count = quicksort(x)
    countlist2.append(count)
print()
print("The mean comparisons of experiments with list size n = 100 is", statistics.mean(countlist2))
print("The median comparisons of experiments with list size n = 100 is", statistics.median(countlist2))
print("The quotient of the mean divided by n log n is" , statistics.mean(countlist2) / (100*math.log(100) ))
print("The quotient of the median divided by n log n is" , statistics.median(countlist2) / (100*math.log(100)) )

for j in range (10):
    x = []
    for i in range (1000):
        x.append(random.randint(1,1000))
    count = quicksort(x)
    countlist3.append(count)
print()
print("The mean comparisons of experiments with list size n = 1000 is", statistics.mean(countlist3))
print("The median comparisons of experiments with list size n = 1000 is", statistics.median(countlist3))
print("The quotient of the mean divided by n log n is" , statistics.mean(countlist3) / (1000*math.log(1000)) )
print("The quotient of the median divided by n log n is" , statistics.median(countlist3) / (1000*math.log(1000) ))

for j in range (10):
    x = []
    for i in range (10000):
        x.append(random.randint(1,10000))
    count = quicksort(x)
    countlist4.append(count)
print()
print("The mean comparisons of experiments with list size n = 10000 is", statistics.mean(countlist4))
print("The median comparisons of experiments with list size n = 10000 is", statistics.median(countlist4))
print("The quotient of the mean divided by n log n is" , statistics.mean(countlist4) / (10000*math.log(10000)) )
print("The quotient of the median divided by n log n is" , statistics.median(countlist4) / (10000*math.log(10000)) )


countlist6 = []
for j in range (10):
    x = []
    for i in range (50000):
        x.append(random.randint(1,50000))
    count = quicksort(x)
    countlist6.append(count)


print()
print("The mean comparisons of experiments with list size n = 50000 is", statistics.mean(countlist6))
print("The median comparisons of experiments with list size n = 50000 is", statistics.median(countlist6))
print("The quotient of the mean divided by n log n is" , statistics.mean(countlist6) / (50000*math.log(50000)) )
print("The quotient of the median divided by n log n is" , statistics.median(countlist6) / (50000*math.log(50000)) )

for j in range (100000):
    x = []
    countlist = []
    for i in range (30):
        x.append(random.randint(1,30))
    count = quicksort(x)
    countlist5.append(count)
print()

print("---Part(c)---")



print()
print("The max number of comparisons divided by n log n in a list of n = 30, ran 100000 times  is", max(countlist5) / (30*math.log(30)))
