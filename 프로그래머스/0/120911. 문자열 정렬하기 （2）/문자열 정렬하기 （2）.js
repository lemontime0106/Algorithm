function solution(my_string) {
    var lowerCaseString = my_string.toLowerCase();
    
    var sortedString = lowerCaseString.split('').sort().join('');
    
    return sortedString;
}