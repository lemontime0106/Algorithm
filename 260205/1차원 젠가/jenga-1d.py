N = int(input())
lst = [int(input()) for _ in range(N)]

lst.reverse()

def remove_range(arr, s, e):
    start = len(arr) - e
    end = len(arr) - s + 1
    del arr[start:end]

s1, e1 = map(int, input().split())
remove_range(lst, s1, e1)

s2, e2 = map(int, input().split())
remove_range(lst, s2, e2)

if lst:
    for x in reversed(lst):
        print(x)
else:
    print(0)
