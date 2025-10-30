# Используем декоратор lru_cache для автоматической мемоизации
from functools import lru_cache
import sys




@lru_cache(maxsize=None)
def catalan_number(n: int) -> int:
    """

    """
    if n < 0:
        raise ValueError("N должно быть неотрицательным целым числом.")

    # Базовый случай: C_0 = 1
    if n == 0:
        return 1

    # Рекурсивный случай: C_n = Sum_{k=0}^{n-1} C_k * C_{n-1-k}
    result = 0
    for k in range(n):
        # Рекурсивный вызов C_k и C_{n-1-k}
        term = catalan_number(k) * catalan_number(n - 1 - k)
        result += term

    return result

