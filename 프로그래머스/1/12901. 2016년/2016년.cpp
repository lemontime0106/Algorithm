#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    vector<int> days = {
        31, 29, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    };
    
    vector<string> week = {
        "FRI", "SAT", "SUN", "MON",
        "TUE", "WED", "THU"
    };
    
    int total = 0;
    
    for (int i = 0; i < a - 1; i++) {
        total += days[i];
    }
    
    total += b - 1;
    
    return week[total % 7];
}