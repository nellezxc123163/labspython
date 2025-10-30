import sys


def find_most_frequent_first_digit():

    try:

        n_input = input("Введите количество чисел N: ")
        N = int(n_input)
    except EOFError:
        print("Ошибка ввода: Не удалось считать N.")
        return
    except ValueError:
        print("Ошибка: N должно быть целым числом.")
        return

    try:
        print(f"Введите {N} целых чисел через пробел или построчно:")

        numbers_input = sys.stdin.read().split()
        A = [int(s) for s in numbers_input[:N]]

    except ValueError:
        print("Ошибка: Все элементы массива должны быть целыми числами.")
        return

    if len(A) < N:
        print(f"Введено только {len(A)} чисел вместо ожидаемых {N}.")
        # Продолжаем работу с тем, что есть
        N = len(A)

    if N == 0:
        print("Массив пуст. Невозможно определить самую частую первую цифру.")
        return


    counts = [0] * 10


    for x in A:

        if x == 0:
            continue


        first_digit = abs(x)


        while first_digit >= 10:
            first_digit //= 10  


        counts[first_digit] += 1


    max_count = -1
    most_frequent_digit = -1

    for digit in range(1, 10):
        if counts[digit] > max_count:
            max_count = counts[digit]
            most_frequent_digit = digit


    print("\n--- Результат ---")
    if most_frequent_digit != -1:
        print(f"Самая частая первая цифра: **{most_frequent_digit}**")
        print(f"Количество элементов, начинающихся с нее: **{max_count}**")
    else:

        print("В массиве не найдено чисел, начинающихся с цифр от 1 до 9.")



find_most_frequent_first_digit()