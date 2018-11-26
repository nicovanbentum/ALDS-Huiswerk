def machtv3(a, n):
    assert n > 0

    m = 1
    multiplication_count = 0

    while n > 0:
        if n%2 == 0:
            a = a*a
            n = n//2
            multiplication_count += 1
        else:
            m = m * a
            n -= 1
            multiplication_count += 1           

    print("calculated result: " + str(m))
    return multiplication_count

print("expected result: " + str(2**3))
print("number of calculations: " + str(machtv3(2,3)))

print("expected result: " + str(2**8))
print("number of calculations: " + str(machtv3(2,8)))

print("expected result: " + str(2**10000))
print("number of calculations: " + str(machtv3(2,10000)))