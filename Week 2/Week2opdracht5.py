import random

cmp_count = 0

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

def qsort(a, low=0,high=-1):
    global cmp_count

    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a, low, random.randint(low,high))
        m = low
        for j in range(low+1, high+1):
            if a[j] < a[low]:
                cmp_count = cmp_count + 1
                m += 1
                swap(a,m,j)
        swap(a,low,m)

        if m > 0:
            qsort(a,low,m-1)
        qsort(a,m+1,high)

#################################################
test_list = []
for _ in range(10000):
    random_integer = random.randint(1, 10000)
    test_list.append(random_integer)

cmp_count = 0
qsort(test_list)
print("number of comparisons: " + str(cmp_count))
if sorted(test_list) != test_list:
    print("The quick sort implementation given in the assignment/reader doesn't actually work..")
else:
    print("list is sorted.")
#################################################

def qsort_worst_pivot(a, low=0,high=-1):
    global cmp_count

    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a, low, high) #instead of a random integer we swap low with high
        m = low
        for j in range(low+1, high+1):
            if a[j] < a[low]:
                cmp_count = cmp_count + 1
                m += 1
                swap(a,m,j)
        swap(a,low,m)

        if m > 0:
            qsort_worst_pivot(a,low,m-1)
        qsort_worst_pivot(a,m+1,high)

#################################################
test_list2 = []
for _ in range(10000):
    random_integer = random.randint(1, 10000)
    test_list2.append(random_integer)

cmp_count = 0
qsort_worst_pivot(test_list2)
print("number of comparisons: " + str(cmp_count))
if sorted(test_list) != test_list:
    print("The quick sort implementation given in the assignment/reader doesn't actually work..")
else:
    print("list is sorted.")
#################################################