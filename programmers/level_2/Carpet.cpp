#include <string>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int area = brown + yellow;

    for(int i = 3; i <= sqrt(area); i++){
        if(area % i == 0){
            int vertical = i;
            int horizontal = area / i;
            if(brown == 2 * horizontal + (vertical - 2) * 2){
                answer.push_back(horizontal);
                answer.push_back(vertical);
                break;
            }
            else{
                continue;
            }
        }
    }
    return answer;
}

int main(){
    vector<int> result = solution(10, 2);
    vector<int> result2 = solution(8, 1);
    vector<int> result3 = solution(24, 24);
    cout << result[0] << "," << result[1] << endl;
    cout << result2[0] << "," << result2[1] << endl;
    cout << result3[0] << "," << result3[1] << endl;
    return 0;
}