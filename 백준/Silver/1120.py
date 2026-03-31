A, B = input().split()

answer = float('inf')

for start in range(len(B) - len(A) + 1):
    diff = 0
    for i in range(len(A)):
        if A[i] != B[start + i]:
            diff += 1
    answer = min(answer, diff)

print(answer)
