#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// phone_book의 번호들 중 특정 번호가 다른 번호의 접두어인 경우가 있는지 찾기
bool solution(vector<string> phone_book) {
    bool answer = true;

    // 오름차순 정렬
    sort(phone_book.begin(), phone_book.end());

    for(int i = 1; i < phone_book.size(); i++){
        // 현재 번호가 이전의 번호로 시작한다면 접두어이므로 정답은 false
        if(phone_book[i].find(phone_book[i - 1]) == 0){//find는 찾는 문자의 첫번째 인덱스 반환
            answer = false;
        }
    }

    return answer;
}

int main(){
    cout << solution({"119", "97674223", "1195524421"}) << endl;
    cout << solution({"123","456","789"}) << endl;
    cout << solution({"12","123","1235","567","88"}) << endl;
    return 0;
}