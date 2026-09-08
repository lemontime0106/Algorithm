#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    set<int> types;
    
    for (int num : nums) {
        types.insert(num);
    }
    
    int maxCount = nums.size() / 2;
    int typeCount = types.size();
    
    
    return min(maxCount, typeCount);
}