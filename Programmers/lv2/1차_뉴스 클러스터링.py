from collections import Counter


def get_str(str):
    tmp = []
    for i in range(len(str) - 1):
        if str[i].isalpha() and str[i + 1].isalpha():
            s = str[i] + str[i + 1]
            tmp.append(s.lower())
    return tmp


def solution(str1, str2):
    answer = 0
    a = get_str(str1)
    b = get_str(str2)

    if not a and not b:
        return 1 * 65536

    min_set = []
    max_set = a[:]

    size = min(len(a), len(b))
    tmp_a = a[:]

    for item in b:
        if item not in tmp_a:
            max_set.append(item)
        else:
            tmp_a.remove(item)

    for item in b:
        if item in a:
            min_set.append(item)
            a.remove(item)

    return int(len(min_set) / len(max_set) * 65536)