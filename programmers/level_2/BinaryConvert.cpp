#include <string>
#include <vector>
#include <iostream>

using namespace std;

// 0과 1로 이루어진 string s에서 0을 제거하고 남은 문자열의 크기를 이진수로 바꾸기
// 1이 될때까지 반복
vector<int> solution(string s) {
    vector<int> answer;
    int convert = 0;
    int zeros = 0;

    while(s != "1"){
        string s_conv = "";

        // 0 제거
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '1'){
                s_conv += s[i];
            }
        }
        // 제거한 0의 개수
        zeros += s.length() - s_conv.length();

        int c = s_conv.length();
        s = "";
        while(c != 0){
            s = to_string(c % 2) + s;
            c /= 2;
        }
        // 변환 횟수 1 증가
        convert++;
    }
    answer.push_back(convert);
    answer.push_back(zeros);

    return answer;
}

int main(){
    vector<int> result1 = solution("110010101001");
    vector<int> result2 = solution("01110");
    vector<int> result3 = solution("1111111");
    
    for(int num : result1){
        cout << num << " ";
    }
    cout << endl;

    for(int num : result2){
        cout << num << " ";
    }
    cout << endl;
    
    for(int num : result3){
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}