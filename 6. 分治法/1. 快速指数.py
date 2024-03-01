def fast_power_flaw(x,n):
    if n <= 0:
        return 1
    elif n == 1:
        return x

    elif n % 2:
        return fast_power_flaw(x * x, n // 2) * x

    else:
        return fast_power_flaw(x * x, n // 2)




a = fast_power_flaw(5,-2)
print(a)