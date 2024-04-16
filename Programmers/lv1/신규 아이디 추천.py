def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    print(1, new_id)
    # 2단계
    tmp_id = ""
    for i in new_id:
        if i.isalpha() or i.isdigit() or i == "-" or i == "_" or i == ".":
            tmp_id += i
    new_id = tmp_id
    print(2, new_id)
    # 3단계
    tmp_id = ""
    for i in range(len(new_id)):
        if new_id[i] == ".":
            if i > 0:
                if new_id[i - 1] == ".":
                    continue
        tmp_id += new_id[i]
    new_id = tmp_id
    print(3, new_id)
    # 4단계
    tmp = ""
    for i in range(len(new_id)):
        if new_id[i] == ".":
            if i == 0 or i == len(new_id) - 1:
                continue
            tmp += new_id[i]
        else:
            tmp += new_id[i]
    new_id = tmp
    print(4, new_id)
    # 5단계
    if not new_id:
        new_id += "a"
    print(5, new_id)
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    print(6, new_id)
    # 7단계
    if len(new_id) <= 2:
        last = new_id[-1]
        print("last", last)
        while len(new_id) < 3:
            new_id += last
    print(7, new_id)

    return new_id