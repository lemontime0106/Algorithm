def is_palindrome(s):
    return s == s[::-1]

T = int(input())

for tc in range(1, T + 1):
    word = input()
    n = len(word)
    mid = n // 2

    left = word[:mid]
    right = word[mid + 1:]

    if is_palindrome(word) and is_palindrome(left) and is_palindrome(right):
        answer = "YES"
    else:
        answer = "NO"

    print(f"#{tc} {answer}")