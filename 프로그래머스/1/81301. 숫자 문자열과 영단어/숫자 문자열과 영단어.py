def solution(s):
    num_word = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
                "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    
    temp = ""
    answer = ""
    
    for char in s:
        if char.isdigit():
            answer += char
        else:
            temp += char
            if temp in num_word:
                answer += num_word[temp]
                temp = ""
    
    return int(answer)