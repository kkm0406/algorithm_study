def solution(friends, gifts):
    answer = 0

    present = {}
    give, receive = {}, {}
    gift_index = {}
    receive_cnt = {}

    for i in friends:
        give[i], receive[i] = 0, 0
        receive_cnt[i] = 0

    for a in friends:
        tmp = {}
        for b in friends:
            if a == b:
                continue
            tmp[b] = 0
        present[a] = tmp

    for gift in gifts:
        a, b = gift.split(" ")
        # a가 준 친구, b가 받은 친구
        present[a][b] += 1

    for key, value in present.items():
        key_give = sum(value.values())
        give[key] = key_give
        for val_key, val_val in value.items():
            receive[val_key] += val_val

    for key, value in give.items():
        gift_index[key] = value - receive[key]

    for a in friends:
        for b in friends:
            if a == b:
                continue
            if present[a][b] > present[b][a]:
                receive_cnt[a] += 1
            if present[b][a] > present[a][b]:
                receive_cnt[b] += 1
            elif (present[a][b] + present[b][a] == 0) or (present[a][b] == present[b][a]):
                if gift_index[a] > gift_index[b]:
                    receive_cnt[a] += 1
                elif gift_index[b] > gift_index[a]:
                    receive_cnt[b] += 1

    return (max(receive_cnt.values()) // 2)
