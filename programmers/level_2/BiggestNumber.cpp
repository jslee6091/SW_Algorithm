#include <string>
#include <vector>
#include <iostream>

using namespace std;

string maximum = "";

/*
bool cmp(char s, char t){
    return s < t;
}
*/

// 숫자로 이루어진 문자열에서 k개의 수를 제거한 후 얻을 수 있는 가장 큰 수(Greedy algorithm)
string solution(string number, int k) {
    string answer = "";
    int starting = k;

    // stack 처럼 answer 문자열의 끝부분에 문자 추가
    for(int i = 0; i < number.length(); i++){
        // answer의 끝문자가 다음 넣을 문자의 크기보다 작을 때 큰 값 나올때까지 제거
        while(starting > 0 && answer.length() > 0 && answer[answer.length() - 1] < number[i]){
            answer = answer.substr(0, answer.length() - 1);
            starting--;
        }

        answer += number[i];
    }

    // 제거 횟수가 k보다 작은 경우 answer의 크기가 정답보다 크므로 초과된 뒷부분을 제거
    if(answer.length() != number.length() - k){
        answer = answer.substr(0, number.length() - k);
    }

    /* cmp 함수와 함께 내가 만든 코드(시간초과 발생해서 인터넷을 검색하여 윗부분 코드 작성)
    string support = number.substr(0, k + 1);

    for(int i = 0; i < number.size() - k; i++){
        string findstr = support;

        sort(findstr.begin(), findstr.end(), cmp);
        answer += findstr[findstr.length() - 1];

        starting = support.find(findstr[findstr.length() - 1]) + 1;
        support = support.substr(starting);
        support += number[k + 1 + i];
    }
    */

    return answer;
}

int main(){
    cout << solution("1924", 2) << endl;
    cout << solution("1231234", 3) << endl;
    cout << solution("4177252841", 4) << endl;
    cout << solution("987654321", 4) << endl;
    return 0;
}