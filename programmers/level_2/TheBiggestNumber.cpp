#include <string>
#include <vector>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

// 0 이상의 양의 정수로 이루어진 배열에서 원소들을 이어 붙여 만들 수 있는 가장 큰 수 구하기

// 정렬 함수 - 두 문자열을 붙일 때 더 큰 순서대로 정렬하기
bool compare(string x, string y){
    return x + y > y + x;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> allnumber;

    // numbers의 원소들을 문자열로 변환하여 저장
    for(int i = 0; i < numbers.size(); i++){
        allnumber.push_back(to_string(numbers[i]));
    }

    // 두개씩 붙였을 때의 모든 경우에 대해 더 큰 수가 나오는 순서대로 정렬
    sort(allnumber.begin(), allnumber.end(), compare);
    
    // 문자열 vector의 첫번째 원소가 "0" 이면 모든 숫자가 0 이므로 0 return
    if(allnumber.at(0) == "0"){
        // "00000" 와 같은 식으로 나오는 것 방지
        return "0";
    }

    // 문자열 vector의 원소들을 순서대로 정답 문자열에 추가
    for(string s : allnumber){
        answer += s;
    }

    return answer;
}

int main(){
    cout << solution({6, 10, 2}) << endl;
    cout << solution({3, 30, 34, 5, 9}) << endl;
    cout << solution({0, 0, 0, 0, 0, 0}) << endl;
    return 0;
}