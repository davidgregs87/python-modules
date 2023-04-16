def factory(n=0):
    if (n % 2 == 0):
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2