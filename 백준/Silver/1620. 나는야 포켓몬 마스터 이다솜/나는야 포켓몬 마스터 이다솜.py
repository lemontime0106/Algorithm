N, M = map(int, input().split())

pedia_by_number = {}
pedia_by_name = {}

for i in range(1, N + 1):
    name = input()
    pedia_by_number[i] = name
    pedia_by_name[name] = i

for _ in range(M):
    query = input()

    if query.isdigit():
        number = int(query)
        if number in pedia_by_number:
            print(pedia_by_number[number])

    else:
        if query in pedia_by_name:
            print(pedia_by_name[query])
