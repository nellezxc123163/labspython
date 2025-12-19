def catalan(n):
    if n <= 1:  # Базовый случай
        return 1
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n - 1 - i)
    return res

