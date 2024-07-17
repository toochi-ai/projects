# Алгоритмы сортировки

# Сортировка пузырьком
# ---------------------

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)

# Сортировка вставками
# ---------------------
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx - 1] > x:
        array[idx] = array[idx - 1]
        idx -= 1
        array[idx] = x

count = 0

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0:
        count += 1
        if array[idx - 1] <= x:
            break
        array[idx] = array[idx - 1]
        idx -= 1
    array[idx] = x

print(count)

