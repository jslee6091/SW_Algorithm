#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(int a, int b) {
    string answer = "";
    vector<int> month = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    vector<string> day = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
    int date = 0;

    for(int i = 0; i < a - 1; i++){
        date += month[i];
    }
    date = (date + b - 1) % 7;
    answer = day[date];

    return answer;
}

int main(){
    cout << solution(5, 24) << endl;
    cout << solution(7, 4) << endl;
    cout << solution(11, 16) << endl;
}