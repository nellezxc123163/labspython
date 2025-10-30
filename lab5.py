import math


product = 1.0


for n in range(1, 11):

    numerator = 3 * (n ** 2) + 2 * n + 1

    denominator = 2 * (n ** 2) + math.sin(2 * (n ** 2))


    term = numerator / denominator


    product *= term


print(f"Вычисленное произведение P для n от 1 до 10:")
print(f"P = {product}")