function solution(my_string) {
    var answer = [];
    
    for (let i = 0; i < my_string.length; i++) {
        let suffix = "";
        
        for (let j = i; j < my_string.length; j++) {
            suffix += my_string[j];
        }
        answer.push(suffix);
    }
    
    answer.sort((a, b) => {
        if (a < b) return -1;
        if (a > b) return 1;
        return 0;
    });
    
    return answer;
}