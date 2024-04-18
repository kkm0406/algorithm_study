from collections import deque


def solution(msg):
    answer = []
    dict = []
    for i in range(26):
        dict.append(chr(ord("A") + i))
    i = 1
    word = msg[0]
    msg = list(msg)
    index = []

    while i < len(msg):
        word += msg[i]
        if word in dict:
            i += 1
        else:
            dict.append(word)
            index.append(dict.index(word[:-1]) + 1)
            word = ""

    index.append(dict.index(word) + 1)
    return index