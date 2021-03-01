def ArrayDiff(a, b):
    result = []
    for elem in a:
        if (elem not in b):
            result.append(elem)

    return result

a = [1, 2, 2, 1, 1, 3, 4, 3, 3, 3, 2, 4]
b = [2, 3, 1]
result = ArrayDiff(a, b)

for elem in result:
    print(elem) 