#include <iostream>
#include <string>
#include <deque>
using namespace std;

// 짝지어 제거하기 문제 - 문자열에서 2번 연속 같은 문자가 있는 경우 제거
int solution(string s)
{
    int answer = 1;
    // 앞뒤로 삽입, 삭제가 가능한 deque 활용
    deque<char> ch;

    // 문자열 s의 모든 문자에 대해
    for(int i = 0; i<s.size(); i++){
        // deque이 비어있거나 마지막 원소가 s의 문자와 다른 경우 deque의 뒤에 삽입
        if(ch.empty() || ch.back() != s[i]){
            ch.push_back(s[i]);
        }
        // deque의 마지막 원소가 s와 같은 경우 deque의 원소 제거, s의 문자 삽입x
        else{
            ch.pop_back();
        }
    }

    // s의 모든 문자를 짝지어 제거하지 못한 경우 정답은 0
    if(ch.size() > 0){
        answer = 0;
    }

    return answer;
}

int main(){
    cout << solution("baabaa") << endl;
    cout << solution("cdcd") << endl;
}