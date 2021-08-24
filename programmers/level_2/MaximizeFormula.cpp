#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

long long maximum = 0;
char ope[3] = {'+', '-', '*'};

// 주어진 수식 문자열을 연산자 우선 순위를 서로 다르게 하여 계산할 때 최대값 구하기
long long get_operate(vector<long long> op2, string s2){
    // 연산 순서가 담긴 문자열 s2에 대해
    for(int i = 0; i < 3; i++){
        // 연산자 s2[i]의 위치 추적
        auto temp2 = find(op2.begin(), op2.end(), int(s2[i]));
        while (temp2 != op2.end()){
            long long temp3 = 0;
            int temp4 = temp2 - op2.begin();

            // 만약 연산자 s2[i] 값이 숫자의 값과 같은 경우
            if(temp4 % 2 == 0){
                // 다음 위치부터 다시 탐색
                temp2 = find(temp2 + 1, op2.end(), int(s2[i]));
                continue;
            }
            
            // 곱셈, 뺄셈, 나눗셈의 경우에 따라 연산
            if(s2[i] == '*'){
                temp3 = op2[temp4 - 1] * op2[temp4 + 1];
            }
            else if(s2[i] == '+'){
                temp3 = op2[temp4 - 1] + op2[temp4 + 1];
            }
            else if(s2[i] == '-'){
                temp3 = op2[temp4 - 1] - op2[temp4 + 1];
            }

            // 원래 연산자가 있던 위치에 새 값을 넣고 앞뒤의 숫자들 제거
            op2[temp4] = temp3;
            op2.erase(op2.begin() + temp4 - 1);
            op2.erase(op2.begin() + temp4);

            // 현재 연산자 s2[i]와 같은 연산자가 있는지 탐색 후 있으면 반복
            temp2 = find(op2.begin(), op2.end(), int(s2[i]));
        }

        // 이미 연산이 끝난 경우 break
        if(op2.size() == 1){
            break;
        }
    }
    
    // 절대 값으로 변환 후 return
    return abs(op2[0]);
}

long long get_permute(vector<long long> op, int* vs, int count, string s){
    // 연산 순서를 모두 정한 경우
    if(count == 3){
        // 연산 실행
        long long temp = get_operate(op, s);
        // 최대값 갱신
        if(maximum < temp){
            maximum = temp;
        }
        return maximum;
    }

    // 덧셈, 뺄셈, 나눗셈에 대한 모든 우선순위 순서를 탐색(순열)
    for(int i = 0; i< 3; i++){
        if(vs[i] == 0){
            vs[i] = 1;
            get_permute(op, vs, count + 1, s + ope[i]);
            vs[i] = 0;
        }
    }
    return maximum;
}

long long solution(string expression) {
    long long answer = 0;
    vector<long long> operands;

    // 수식 문자열을 숫자와 연산자로 분리하여 vector에 저장
    int index = 0;
    for(int i = 0; i < expression.size(); i++){
        if(expression[i] == '/' or expression[i] == '*' or expression[i] == '+' or expression[i] == '-'){
            // 숫자 저장
            operands.push_back(atoi(expression.substr(index, i + 1).c_str()));
            // 연산자 저장(char이 long long으로 자동 변환됨)
            operands.push_back(expression[i]);
            index = i + 1;
        }
    }
    // 마지막 숫자 저장
    operands.push_back(atoi(expression.substr(index).c_str()));

    int visits[3] = {0, };

    answer = get_permute(operands, visits, 0, "");
    return answer;
}