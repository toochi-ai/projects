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


# Сортировка слиянием
# --------------------

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
