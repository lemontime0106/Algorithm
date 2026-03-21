N = int(input())

nums = set()

for i in range(N+1):
    for v in range(N+1-i):
        for x in range(N+1-i-v):
            l = N-i-v-x

            value = i * 1 + v * 5 + x * 10 + l * 50
            nums.add(value)

print(len(nums))