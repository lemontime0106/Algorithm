function solution(my_strings, parts) {
    var answer = '';
    
    for (let i = 0; i < parts.length; i++) {
        const word = my_strings[i]
        const [s, e] = parts[i]
        
        // for (let j = s; j < e+1; j++) {
        //     answer += word[j]
        // }
        answer += word.slice(s, e+1)
    }
    return answer;
}