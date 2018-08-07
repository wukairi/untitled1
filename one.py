


def two( x , n ):
    s = x
    while n > 1:
        n = n - 1
        s = s * x
    return s


print(two(5,3))