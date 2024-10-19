function solution(users, emoticons) {
    let answer = [0, 0];
    const percent = [10, 20, 30, 40];
    let discount = [];
    
    function dfs(stack) {
        if (stack.length === emoticons.length) {
            discount.push([...stack]);
            return;
        }
        for (let i = 0; i < 4; i++) {
            stack.push(percent[i]);
            dfs(stack);
            stack.pop();
        }
    }
    
    dfs([]);
    
    for (let discounts of discount) {
        let plus = 0;
        let profit = 0;
        
        for (let user of users) {
            let temp = 0;
            for (let j = 0; j < emoticons.length; j++) {
                if (discounts[j] >= user[0]) {
                    temp += emoticons[j] * ((100 - discounts[j]) / 100);
                }
            }
            if (user[1] <= temp) {
                plus += 1;
            } else {
                profit += temp;
            }
        }
        
        if (answer[0] < plus) {
            answer = [plus, Math.floor(profit)];
        } else if (answer[0] === plus) {
            if (answer[1] < profit) {
                answer = [plus, Math.floor(profit)];
            }
        }
    }
    
    return answer;
}