cnt = 0
total = 0

score = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

for _ in range(20):
    a, b, c = input().split()

    if c == "P":
        continue

    cnt += float(b)
    total += float(b) * score[c]

print(f"{total / cnt:.6f}" if cnt > 0 else 0)
