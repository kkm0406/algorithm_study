def solution(bandage, health, attacks):
    answer = 0
    arr = [[0, 0] for _ in range(attacks[-1][0] + 1)]
    for attack in attacks:
        arr[attack[0]][0] = attack[0]
        arr[attack[0]][1] = attack[1]

    print(arr)
    seq = 0
    # arr[i][0]: 공격시간, arr[i][1]: 피해량
    # bandage는 [시전 시간, 초당 회복량, 추가 회복량]
    now = health
    for i in range(1, attacks[-1][0] + 1):
        if arr[i][0] == 0:  # 공격시간이 아니면
            seq += 1  # 연속 성공 + 1
            if seq == bandage[0]:
                if now + bandage[1] + bandage[2] <= health:
                    now += bandage[1] + bandage[2]
                else:
                    now = health
                seq = 0
            else:
                if now + bandage[1] <= health:
                    now += bandage[1]  # 연속 성공한 만큼 체력 추가
                else:
                    now = health
        else:  # 공격시간이면
            seq = 0
            now -= arr[i][1]
            if now <= 0:
                break

    return -1 if now <= 0 else now

