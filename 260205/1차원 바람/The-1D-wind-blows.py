N, M, Q = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

winds = []

def change(lst, direct):
    if direct == "L":
        lst.insert(0, lst.pop())
    else:
        lst.append(lst.pop(0))

def is_possible(a, b):
    for i in range(M):
        if a[i] == b[i]:
            return True
    return False

for _ in range(Q):
    f, direct = input().split()
    floor = int(f) - 1

    change(MAP[floor], direct)

    cur_dir = direct
    cur = floor

    while cur - 1 >= 0:
        if not is_possible(MAP[cur], MAP[cur-1]):
            break
        
        cur_dir = "L" if cur_dir == "R" else "R"
        change(MAP[cur-1], cur_dir)
        cur -= 1
    
    cur_dir = direct
    cur = floor

    while cur + 1 < N:
        if not is_possible(MAP[cur], MAP[cur+1]):
            break
        
        cur_dir = "L" if cur_dir == "R" else "R"
        change(MAP[cur+1], cur_dir)
        cur += 1

for i in MAP:
    print(*i)