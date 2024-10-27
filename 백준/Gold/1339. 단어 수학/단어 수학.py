N = int(input())
word = [input() for _ in range(N)]

alphabet = {}

for w in word:
    length = len(w) - 1
    for i in w:
        if i in alphabet:
            alphabet[i] += 10 ** length
        else:
            alphabet[i] = 10 ** length
        length -= 1

answer = 0
number = 9
sorted_alphabet = sorted(alphabet.values(), reverse=True)

for i in sorted_alphabet:
    answer += i * number
    number -= 1

print(answer)