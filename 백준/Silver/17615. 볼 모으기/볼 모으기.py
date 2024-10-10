N = int(input())
lst = input().strip()

answer = []

red_right = lst.rstrip("R")
answer.append(red_right.count("R"))

blue_right = lst.rstrip("B")
answer.append(blue_right.count("B"))

red_left = lst.lstrip("R")
answer.append(red_left.count("R"))

blue_left = lst.lstrip("B")
answer.append(blue_left.count("B"))

print(min(answer))