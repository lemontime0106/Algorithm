arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    arr.append(arr[i-2] + arr[i-3])

for _ in range(int(input())):
    print(arr[int(input())])
