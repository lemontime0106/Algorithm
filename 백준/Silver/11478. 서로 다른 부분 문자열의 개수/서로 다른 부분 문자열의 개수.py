S = input()
string_set = set()

for i in range(1, len(S) + 1):
    for j in range(len(S) - i + 1):
        substring = S[j:j + i]
        string_set.add(substring)

print(len(string_set))
