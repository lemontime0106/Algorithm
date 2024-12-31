N = int(input())
expression = list(input())
num = [int(input()) for _ in range(N)]

stack = []

for i in expression:
    if i.isalpha():
        stack.append(num[ord(i) - 65])

    else:
        temp = stack.pop()
        result = stack.pop()

        if i == "+":
            result += temp

        elif i == "-":
            result -= temp

        elif i == "*":
            result *= temp

        elif i == "/":
            result /= temp

        stack.append(result)

print("%.2f" %stack[-1])