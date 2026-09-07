#include <string>
#include <vector>

using namespace std;

int solution(vector<int> arr1, vector<int> arr2) {
    int a = arr1.size();
    int b = arr2.size();
    
    int sum_a = 0;
    int sum_b = 0;
    
    for (int a1 : arr1) {
        sum_a += a1;
    }
    
    for (int a2 : arr2) {
        sum_b += a2;
    }
    
    if (a != b) {
        if (a > b) {
            return 1;
        } else {
            return -1;
        }
    } else {
        if (sum_a > sum_b) {
            return 1;
        } else if (sum_a < sum_b) {
            return -1;
        } else {
            return 0;
        }
    }
    
}