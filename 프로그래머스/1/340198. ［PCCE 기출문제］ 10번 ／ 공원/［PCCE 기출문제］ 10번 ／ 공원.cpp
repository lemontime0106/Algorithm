#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> mats, vector<vector<string>> park) {
    sort(mats.rbegin(), mats.rend());
    
    int row = park.size();
    int col = park[0].size();
    
    for (int size : mats) {
        for (int i = 0; i + size <= row; i++) {
            for (int j = 0; j + size <= col; j++) {
                bool possible = true;
                
                for (int r = i; r < i + size; r++) {
                    for (int c = j; c < j + size; c++) {
                        
                        if (park[r][c] != "-1") {
                            possible = false;
                            break;
                        }
                    }
                    
                    if (!possible) {
                        break;
                    }
                }

                if (possible) {
                    return size;
                }
            }
        }
    }
    
    return -1;
}