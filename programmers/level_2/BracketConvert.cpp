#include <string>
#include <vector>
#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;

// 괄호 문자열을 균형 잡힌 괄호 문자열과 나머지로 분리하는 함수
void separate(string pp, string* u, string* v){
    pair<int, int> bracket = make_pair(0, 0);

    // separate p to u and v
    for(int i = 0; i< pp.size(); i++){
        if(pp[i] == '('){
            bracket.first++;
        }
        else{
            bracket.second++;
        }

        // '('와 ')' 의 개수가 같으면 u와 v에 문자열 저장 후 break
        if(bracket.first == bracket.second){
            *u = pp.substr(0, i + 1);
            *v = pp.substr(i + 1);
            break;
        }
    }   
}

// 괄호 문자열이 올바른 지 확인하는 함수
bool check_bracket(string u){
    // check u is right bracket string
    stack<int> stk;

    bool u_check = true;
    for(int i = 0; i< u.size(); i++){
        // '('인 경우 stack에 저장
        if(u[i] == '('){
            stk.push(u[i]);
        }
        // ')'이고 stack이 비어있지 않으면 top 위치의 원소 삭제
        else if(!stk.empty()){
            stk.pop();
        }
        // ')'인데 stack이 비어있으면 올바른 괄호식이 아니므로 false
        else if(stk.empty()){
            u_check = false;
            break;
        }
    }

    /*
        원래 보통 괄호식이 올바른지 확인할 때는 모든 괄호식을 탐색한 후 stack에
        원소가 남는 경우까지 고려해야 하지만 이 문제의 경우 '(' 와 ')'의 개수가
        항상 같으므로 고려하지 않음
    */
    
    return u_check;
}

// 균형 잡힌 괄호 문자열을 올바른 괄호 문자열로 바꾸는 함수
string convert(string p2){
    string u = "";
    string v = "";

    // 길이가 0 이면 "" return
    if(p2.length() == 0){
        return "";
    }

    // 괄호 문자열을 u와 v로 분리
    separate(p2, &u, &v);

    // u가 올바른 괄호 문자열이면
    if(check_bracket(u)){
        // u와 v를 올바른 괄호 문자열로 바꾼 결과를 합쳐서 return
        return u + convert(v);
    }
    // 균형 잡힌 괄호 문자열인 경우
    else{
        // u의 앞과 뒤 문자를 제거
        u.pop_back();
        u = u.substr(1);

        // 문자열의 모든 괄호의 방향을 바꾸기
        for(int i = 0; i < u.size(); i++){
            if(u[i] == '('){
                u[i] = ')';
            }
            else{
                u[i] = '(';
            }
        }
        // '(' 와 v를 올바른 괄호 문자열로 바꾼 것과 ')'와 u를 합쳐서 return
        return '(' + convert(v) + ')' + u;
    }

}

string solution(string p) {
    string answer = "";

    // p가 ""인 경우 정답은 ""
    if(p.length() == 0){
        return answer;
    }

    // p가 올바른 괄호 문자열이면 p를 바로 return
    if(check_bracket(p)){
        return p;
    }

    answer = convert(p);

    return answer;
}

int main(){
    cout << solution("(()())()") << endl;
    cout << solution(")(") << endl;
    cout << solution("()))((()") << endl;
    return 0;
}