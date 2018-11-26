def machtv3(a, n):
    assert n > 0

    m = 0
    an = a
    while n > 0:
        if n%2 == 0:
            n = n // 2
            an = (a*a)*n
            m += 1

        else:
            n = n - 1
            an = a * (a*a)
            m += 1            

    print("calculated result: " + str(an))
    return m

print("expected result: " + str(2**3))
print("number of calculations: " + str(machtv3(2,3)))