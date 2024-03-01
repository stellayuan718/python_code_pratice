# 数质数
def count_prime(n):
    is_prime = [True] * (n + 1)
    i = 2
    while (i * i <= n):
        if (is_prime[i]):
            j = i
            while (j * i <= n):
                is_prime[i * j] = False
                j += 1
        i += 1

    count = 0
    for i in range(2, n + 1):
        if (is_prime[i]):
            count += 1
            print(i, end=" ")

    return count

a = count_prime(17)
print(a)