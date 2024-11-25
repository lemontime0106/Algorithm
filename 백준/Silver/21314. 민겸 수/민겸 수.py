word = input()

cnt = 0
_max = ""
_min = ""

for w in word:
    if w == "M":
        cnt += 1
    else:
        if cnt > 0:
            _max += str(5 * (10 ** cnt))
            _min += str(10 ** cnt + 5)
        else:
            _max += "5"
            _min += "5"
        cnt = 0

if cnt:
    _max += "1" * cnt
    _min += str(10 ** (cnt - 1))

print(_max)
print(_min)