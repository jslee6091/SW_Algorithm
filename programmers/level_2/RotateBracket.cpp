#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std;

// 괄호 문자열 올바른지 검사
bool isBracket(string ss){
    stack<char> stk;

    for(int i = 0; i < ss.size(); i++){
        // 왼쪽 괄호이면 stack에 push
        if(ss[i] == '[' or ss[i] == '(' or ss[i] == '{'){
            stk.push(ss[i]);
        }
        // 오른쪽 괄호인데 stack에 아무것도 없는 경우 false
        else if(stk.size() == 0){
            return false;
        }
        else{
            char check = stk.top();
            // 오른쪽 괄호와 왼쪽 괄호의 짝이 맞는 경우 stack의 top 제거
            if(check == '[' and ss[i] == ']'){
                stk.pop();
            }
            else if(check == '{' and ss[i] == '}'){
                stk.pop();
            }
            else if(check == '(' and ss[i] == ')'){
                stk.pop();
            }
            // 짝이 안맞으면 false
            else{
                return false;
            }
        }
    }

    // 왼쪽과 오른쪽 괄호의 숫자가 달라서 stack의 크기가 1이상인 경우 false
    if(stk.size() > 0){
        return false;
    }

    // 지금까지 모든 조건 만족하면 true
    return true;
}

int solution(string s) {
    int answer = 0;

    for(int i = 0; i < s.size(); i++){
        // 문자열 s가 올바른 괄호 문자열이면 1 증가
        if(isBracket(s) == true){
            answer++;
        }
        // 문자열 왼쪽으로 1칸 회전
        rotate(s.begin(), s.begin() + 1, s.end());
    }

    return answer;
}

int main(){
    cout << solution("[](){}") << endl;
    cout << solution("}]()[{") << endl;
    cout << solution("[)(]") << endl;
    cout << solution("}}}") << endl;
    return 0;
}