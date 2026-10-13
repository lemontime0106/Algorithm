#include <string>
#include <vector>

using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";
    
    for (char c : s) {
        int cnt = 0;
        
        while (cnt < index) {
            c = 'a' + (c - 'a' + 1) % 26;
            
            if (skip.find(c) != string::npos) {
                continue;
            }
            
            cnt++;
        }
        
        answer += c;
    }
    
    return answer;
}