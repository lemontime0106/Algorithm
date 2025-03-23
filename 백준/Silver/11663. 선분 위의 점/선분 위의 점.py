N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def start(location, target):
    s, e = 0, N-1

    while s <= e:
        mid = (s + e) // 2
        if location[mid] < target:
            s = mid + 1
        else:
            e = mid - 1

    return s

def end(location, target):
    s, e = 0, N-1
    while s <= e:
        mid = (s + e) // 2
        if location[mid] <= target:
            s = mid + 1
        else:
            e = mid - 1
    return s


for _ in range(M):
    a, b = map(int, input().split())
    start_idx = start(lst, a)
    end_idx = end(lst, b)

    print(end_idx - start_idx)