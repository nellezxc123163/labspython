
try:
    N = int(input("Введите количество целых чисел (N): "))


    if N < 0:
        print("Количество чисел N не может быть отрицательным. Установлено N = 0.")
        N = 0

except ValueError:
    print("Ошибка ввода. Введено не целое число для N.")
    N = 0


negative_count = 0


print(f"Введите {N} целых чисел:")

# Используем цикл for для N итераций
for i in range(N):
    try:

        num = int(input(f"Введите число №{i + 1}: "))


        if num < 0:
            negative_count += 1

    except ValueError:
        print("Внимание: Введено некорректное число. Пропускаем.")



print("\n--- Результат ---")
print(f"Количество отрицательных элементов в последовательности: {negative_count}")