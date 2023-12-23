def circular_moves(lst, m):
    path = []
    current_index = 0
    length = len(lst)

    for _ in range(length):
        path.append(lst[current_index])

        # Сдвигаемся интервалом длины m
        current_index = (current_index + m) % length
        print(lst)
        if current_index == 0:
            break  # Прерываем цикл, если вернулись к началу массива

    return path

length = int(input("Введите длину массива: "))
lst = list(map(int, input("Введите элементы массива через пробел: ").split()))
m = int(input("Введите длину интервала m: "))

result = circular_moves(lst, m)
print(result)


"""length = int(input())
lst = list(map(int, input().split()))
shift = int(input())

lst = lst[-shift:] + lst[:-shift]
print(lst)
lst = lst[-shift:] + lst[:-shift]
print(lst)
lst = lst[-shift:] + lst[:-shift]
print(lst)"""
"""def circular_moves(m, n):
    array = list(range(1, m + 1))
    result = []

    for _ in range(n):
        result.append(array[:n])
        lst = [1, 2, 3, 4, 5]shift = 2lst = lst[-shift:] + lst[:-shift]print(lst)

    return result

m = 5
n = 3
result = circular_moves(m, n)
for move in result:
    print(move)
"""