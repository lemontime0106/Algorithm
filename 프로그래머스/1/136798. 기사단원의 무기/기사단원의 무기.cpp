#include <string>
#include <vector>

using namespace std;

int solution(int number, int limit, int power) {
    int answer = 0;
    
    vector<int> cnt;
    
    for (int num = 1; num <= number; num++) {
        int temp = 0;
        
        for (int i = 1; i <= num; i++) {
            if (num % i == 0) {
                temp++;
            }
        }
        
        if (temp > limit) {
            answer += power;
        } else {
            answer += temp;
        }
    }
    
    return answer;
}