# 1.task 0
# Создайте массив из чисел от 1 до 10. Увеличьте каждое число на 3 и выведите результат.
arr = np.arange(1, 11)
arr = arr + 3
print(arr)

# 2.task 0
# Создайте массив из трех строк по 5 нулей. Измените элемент во втором ряду и третьем столбце на 7.
arr = np.zeros((3, 5))
arr[1, 2] = 7
print(arr)

# 3.task 0
# Создайте одномерный массив с числами от 1 до 9. Преобразуйте его в двумерный массив размером 3x3.
arr = np.arange(1, 10)
arr = np.reshape(arr, (3, 3))
print(arr)

# 4.task 0
# Создайте массив из 10 случайных чисел в диапазоне от 0 до 1. Округлите числа до двух знаков после запятой.
arr = np.random.rand(10)
arr = np.round(arr, 2)
print(arr)

# 5.task 0
# Создайте массив из единиц размером 4x4. Измените каждый элемент в первой строке на 3.
arr = np.ones((4, 4))
arr[0, :] = 3
print(arr)

# 6.task 0
# Создайте массив, содержащий только четные числа от 2 до 20. Умножьте каждый элемент массива на 2.
arr = np.arange(2, 21, 2)
arr = arr * 2
print(arr)

# 7.task 0
# Создайте массив из 10 случайных чисел в диапазоне от 0 до 1. Округлите числа до двух знаков после запятой.
arr = np.random.rand(10)
arr = np.round(arr, 2)
print(arr)

# 8.task 0
# Создайте массив из 5 элементов, заполненный случайными числами от 0 до 100. Найдите минимальное и максимальное значения.
arr = np.random.randint(0, 101, 5)
print("Min:", np.min(arr), "Max:", np.max(arr))

# 9.task 0
# Создайте массив размером 3x3, заполненный случайными числами. Найдите среднее значение всех элементов.
arr = np.random.rand(3, 3)
print("Среднее:", np.mean(arr))

# 10.task 0
# Создайте массив из чисел от 0 до 100 с шагом 5. Используйте условие для выбора элементов, которые кратны 10.
arr = np.arange(0, 101, 5)
arr = arr[arr % 10 == 0]
print(arr)

# 11.task
# Создайте массив из 8 случайных чисел и отсортируйте его в порядке убывания.
arr = np.random.rand(8)
arr_sorted = np.sort(arr)[::-1]
print(arr_sorted)

# 12.task
# Создайте двумерный массив размером 5x5, заполненный случайными числами от 0 до 50. Измените все элементы на четных позициях на -1.
arr = np.random.randint(0, 51, (5, 5))
arr[::2, ::2] = -1
print(arr)

# 13.task
# Создайте два массива из 10 случайных чисел. Выведите их поэлементную сумму и разность.
arr1 = np.random.rand(10)
arr2 = np.random.rand(10)
print("Сумма:", arr1 + arr2)
print("Разность:", arr1 - arr2)

# 14.task
# Создайте массив из чисел от 1 до 12 и преобразуйте его в массив 3x4. Затем выведите только элементы, которые больше среднего значения этого массива.
arr = np.arange(1, 13).reshape(3, 4)
mean_value = np.mean(arr)
arr_filtered = arr[arr > mean_value]
print(arr_filtered)

# 15.task
# Создайте массив из чисел от 1 до 30. Преобразуйте его в массив 3x2x5 и найдите сумму элементов, у которых сумма индексов кратна 3.
arr = np.arange(1, 31).reshape(3, 2, 5)
s = 0
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        for k in range(arr.shape[2]):
            if (i + j + k) % 3 == 0:
                s += arr[i, j, k]
print(s)

# 16.task
# Создайте два массива: первый — из чисел от 1 до 9, второй — из чисел от 9 до 1. Найдите элементы, которые больше среднего значения в обоих массивах, и создайте новый массив из этих элементов.
arr1 = np.arange(1, 10)
arr2 = np.arange(9, 0, -1)
mean_arr1 = np.mean(arr1)
mean_arr2 = np.mean(arr2)
new_arr = np.concatenate((arr1[arr1 > mean_arr1], arr2[arr2 > mean_arr2]))
print(new_arr)

# 17.task
# Создайте массив размером 4x4, заполненный случайными числами. Замените все элементы, которые больше медианы этого массива, на их квадрат.
arr = np.random.rand(4, 4)
median_value = np.median(arr)
arr[arr > median_value] = arr[arr > median_value] ** 2
print(np.round(arr, 2))

# 18.task

# 19.task

# 20.task

# 21.task

# 22.task

# 23.task

# 24.task

