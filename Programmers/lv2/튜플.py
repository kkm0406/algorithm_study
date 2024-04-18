def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=lambda x: len(x))
    size = len(s[-1].split(","))
    for item in s:
        item = item.split(",")
        for i in item:
            if int(i) not in answer:
                answer.append(int(i))
            if len(answer) == size:
                break

    return answer