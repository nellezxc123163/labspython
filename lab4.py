
total_sum = 0.0
x = 0.2
for n in range(1, 31):

    power = 2 * n - 1
    term = (x ** power) / power

    total_sum += term

print(f"Сумма 30 членов ряда: {total_sum}")