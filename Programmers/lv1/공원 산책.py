dirs = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}


def solution(park, routes):
    answer = []
    sx, sy = 0, 0
    r = len(park)
    c = len(park[0])
    for i in range(r):
        for j in range(c):
            if park[i][j] == "S":
                sx, sy = i, j
                break

    for route in routes:
        op, n = route.split(" ")
        dx, dy = dirs[op]
        tmp_x, tmp_y = sx, sy
        flag = True
        for i in range(int(n)):
            if 0 <= tmp_x + dx < r and 0 <= tmp_y + dy < c:
                if park[tmp_x + dx][tmp_y + dy] != "X":
                    tmp_x += dx
                    tmp_y += dy
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            sx, sy = tmp_x, tmp_y

    return [sx, sy]