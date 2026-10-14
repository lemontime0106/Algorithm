#include <string>
#include <vector>

using namespace std;

int solution(vector<int> ingredient) {
    int answer = 0;
    vector<int> st;
    
    for (int x : ingredient) {
        st.push_back(x);
        
        int n = st.size();
        
        if (n >= 4) {
            if (st[n-4] == 1 &&
                st[n-3] == 2 &&
                st[n-2] == 3 &&
                st[n-1] == 1) {
                
                for (int i = 0; i < 4; i++) {
                    st.pop_back();
                }
                answer++;
            }
        }
    }
    
    return answer;
}