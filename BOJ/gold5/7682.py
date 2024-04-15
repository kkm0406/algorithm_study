# 틱택토
# 구현
import sys

input = sys.stdin.readline


def tictactoe(case, typ):
    if case[0] == typ and case[0] == case[1] == case[2]:
        return True
    elif case[0] == typ and case[0] == case[3] == case[6]:
        return True
    elif case[4] == typ and case[1] == case[4] == case[7]:
        return True
    elif case[4] == typ and case[3] == case[4] == case[5]:
        return True
    elif case[8] == typ and case[6] == case[7] == case[8]:
        return True
    elif case[8] == typ and case[2] == case[5] == case[8]:
        return True
    elif case[4] == typ and case[0] == case[4] == case[8]:
        return True
    elif case[4] == typ and case[2] == case[4] == case[6]:
        return True
    else:
        return False


while True:
    s = input().strip()
    if s == "end":
        break

    cnt_x = s.count('X')
    cnt_o = s.count('O')

    if cnt_x == cnt_o + 1 or cnt_x == cnt_o:
        type1, type2 = ("X", "O") if cnt_x == cnt_o + 1 else ("O", "X")
        result1 = tictactoe(s, type1)
        result2 = tictactoe(s, type2)

        if result2:
            print("invalid")
        elif not result1:
            if s.count(".") == 0:
                print("valid")
            else:
                print("invalid")
        else:
            print("valid")

    else:
        print("invalid")
