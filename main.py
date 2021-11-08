def rot(num):
    num_list = list(str(num))
    for index, value in enumerate(num_list):
        if value == '6':
            num_list[index] = '9'
            break
    return int("".join([str(l) for l in num_list]))
def medians(n, m):
    c = n + m
    c.sort()
    print(c)
    length = len(c)
    if length % 2 == 0:
        return (c[int(length / 2) - 1] + c[int(length / 2)]) / 2
    else:
        return c[int(length / 2)]