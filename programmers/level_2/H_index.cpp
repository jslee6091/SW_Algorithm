#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// H-index : citations의 원소중 h이상의 원소가 h개 이상, 나머지가 h 이하를 만족하는 h 최대값
int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(), citations.end());

    int h = 0;
    while(true){
        int up = 0;
        int down = 0;

        for(int i = 0; i < citations.size(); i++){
            if(citations[i] >= h){
                down = i;
                up = citations.size() - i;
                break;
            }
        }

        // down 조건 필요없음
        if(up >= h && down <= h){
            answer = h;
            h++;
            continue;
        }
        else{
            break;
        }
    }
    return answer;
}

// 다른 사람의 풀이 참고 - 매우 간단 명료해서 인상 깊었던 코드
int refersolution(vector<int> citations){
    int answer = 0;

    std::sort(citations.begin(), citations.end());
    for (int i = 0; i < citations.size(); i++) {
        if (citations.size() - i <= citations[i]) {
            answer = citations.size() - i;
            break;
        }
    }

    return answer;
}

/*
    문제의 조건을 잘못 이해해서 down이란 변수와 조건을 추가했는데 이것은 필요없다.
    운이 좋게도 solution함수로 통과는 했지만 맞는 풀이는 refersolution인 것 같다.
*/

int main(){
    cout << solution({3, 0, 6, 1, 5}) << endl;
    cout << solution({12, 4, 7, 7, 3, 6, 9, 3}) << endl;
    cout << refersolution({4, 8, 3, 6, 2, 11, 5}) << endl;
    return 0;
}