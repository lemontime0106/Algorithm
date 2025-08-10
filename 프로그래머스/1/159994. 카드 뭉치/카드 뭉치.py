def check(lst1, lst2, word):
    for w in word:
        if lst1 and lst1[0] == w:
            lst1.pop(0)
        elif lst2 and lst2[0] == w:
            lst2.pop(0)
        else:
            return "No"
    return "Yes"

def solution(cards1, cards2, goal):
    return check(cards1, cards2, goal)