def goldbach(n):
    is_primes = [True] * (n + 1)
    i = 2
    while (i * i <= n):
        if (is_primes[i]):
            j = i
            while (j * i <= n):
                is_primes[j * i] = False
                j += 1
        i += 1
    count = 0
    for i in range(2, len(is_primes)):
        if (is_primes[i]):
            count += 1

    primes = [False] * count
    idx = 0
    for i in range(2,len(is_primes)):
        if (is_primes[i]):
            primes[idx] = i
            idx += 1
    left = 0
    right = count - 1
    while (left < right):
        if (n == primes[left] + primes[right]):
            print(n, '=', left, '+', right)
            left += 1
            right -= 1
        elif (n < primes[left] + primes[right]):
            right -= 1
        elif (n > primes[left] + primes[right]):
            left += 1


goldbach(100)