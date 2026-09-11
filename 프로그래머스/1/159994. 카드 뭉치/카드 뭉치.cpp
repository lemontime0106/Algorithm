#include <string>
#include <vector>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    string answer = "Yes";
    
    bool flag = true;
    
    for (string g : goal) {
        if (!cards1.empty() && cards1[0] == g) {
            cards1.erase(cards1.begin());
        } else if (!cards2.empty() && cards2[0] == g) {
            cards2.erase(cards2.begin());
        } else {
            flag =  false;
        }
        
        if (!flag) {
            answer = "No";
            break;
        }
    }
    
    return answer;
}