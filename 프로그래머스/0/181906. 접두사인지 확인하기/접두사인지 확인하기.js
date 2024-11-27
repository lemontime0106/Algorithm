function solution(my_string, is_prefix) {
    var answer = 0;
    
    let prefix = ""
    
    for (let i=0; i < is_prefix.length; i++) {
        prefix += my_string[i]
    } 
    
    if (prefix === is_prefix) {
        answer = 1
    }
    
    return answer;
}