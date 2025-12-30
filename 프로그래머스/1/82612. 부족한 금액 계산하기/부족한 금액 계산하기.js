function solution(price, money, count) {
    let temp = 0;
    
    for (i=1; i <= count; i++) {
        temp = temp + (price * i)
    }
    
    if (temp == money || money > temp) {
        return 0
    } else {
        return Math.abs(temp - money)
    }
}