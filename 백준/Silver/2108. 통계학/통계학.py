from collections import Counter

lst = [int(input()) for _ in range(int(input()))]
lst.sort()

N = len(lst)

def avg1():
    print(round(sum(lst) / N))

def avg2():
    print(lst[N//2])

def avg3():
    counter = Counter(lst)
    most_common = counter.most_common()  # 빈도수 높은 순으로 정렬됨
    most_common.sort(key=lambda x: (-x[1], x[0]))  # 빈도수 내림차순, 숫자 오름차순 정렬

    # 최빈값이 여러 개일 경우 두 번째로 작은 값 선택
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        print(most_common[1][0])  # 두 번째로 작은 최빈값 출력
    else:
        print(most_common[0][0])  # 최빈값이 하나만 존재하면 출력


def avg4():
    print(lst[-1] - lst[0])

avg1()
avg2()
avg3()
avg4()