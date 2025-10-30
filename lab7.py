try:
    N = int(input("Введите количество элементов N (целое число): "))
    if N <= 0:
        print("N должно быть положительным числом.")
        exit()
    arr = []
    print(f"Введите {N} вещественных чисел:")
    for i in range(N):
        element = float(input(f"Элемент {i + 1}: "))
        arr.append(element)
except ValueError:
    print("Ошибка ввода. Убедитесь, что вводите корректные числа.")
    exit()
try:
    X = float(input("\nВведите вещественное число X (начало отрезка): "))
    Y = float(input("Введите вещественное число Y (конец отрезка): "))
    if X > Y:
        X, Y = Y, X
        print(f"Порядок X и Y был скорректирован: X={X}, Y={Y}")
    product_in_range = 1.0
    found_elements = False  # Флаг для отслеживания наличия элементов в отрезке
    for element in arr:
        if X <= element <= Y:
            product_in_range *= element
            found_elements = True
    print("\n--- Результат (Пункт 3) ---")
    print(f"Отрезок: [{X}, {Y}]")
    if not found_elements:
        print("В заданном отрезке нет элементов. Произведение = 1.0 (по определению пустого произведения).")
        print(f"Фактическое произведение: 1.0")
    else:
        print(f"Произведение элементов, принадлежащих отрезку: {product_in_range}")
except ValueError:
    print("Ошибка ввода для X или Y.")