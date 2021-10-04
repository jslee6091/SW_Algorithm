#include <string>
#include <set>
#include <tuple>
#include <iostream>
using namespace std;

// (0,0)에서 위, 아래, 좌, 우 방향으로 이동하며 지나갔던 길의 수를 구하기
// 두번 이상 지나간 길은 한번만 간것으로 설정
int solution(string dirs) {
    int answer = 0;
    set<tuple<int, int, char>> st;
    int x = 0;
    int y = 0;

    for(int i = 0; i < dirs.length(); i++){

        if(dirs[i] == 'U' && y + 1 <= 5){
            st.insert(make_tuple(x, y, 'U'));
            st.insert(make_tuple(x, y + 1, 'D'));
            y++;
        }
        else if(dirs[i] == 'L' && x - 1 >= -5){
            st.insert(make_tuple(x, y, 'L'));
            st.insert(make_tuple(x - 1, y, 'R'));
            x--;
        }
        else if(dirs[i] == 'R' && x + 1 <= 5){
            st.insert(make_tuple(x, y, 'R'));
            st.insert(make_tuple(x + 1, y, 'L'));
            x++;
        }
        else if(dirs[i] == 'D' && y - 1 >= -5){
            st.insert(make_tuple(x, y, 'D'));
            st.insert(make_tuple(x, y - 1, 'U'));
            y--;
        }
    }
    answer = st.size() / 2;
    return answer;
}

int main(){
    cout << solution("ULURRDLLU") << endl;
    cout << solution("LULLLLLLU") << endl;
    return 0;
}