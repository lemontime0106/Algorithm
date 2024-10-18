function solution(sequence, k) {
    let left = 0, right = 0;
    let sum_ = sequence[0];
    let answer = [0, sequence.length]
    
    while (left < sequence.length) {
        if (sum_ < k && right < sequence.length) {
            right += 1
            sum_ += sequence[right]
        } else if (sum_ === k && right - left < answer[1] - answer[0]) {
            answer = [left, right]
            right += 1
            sum_ += sequence[right]
        } else {
            left += 1
            sum_ -= sequence[left - 1]
        }
        }
    return answer;
    }