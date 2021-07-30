#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    // 2차원 벡터 - 각 키패드 숫자의 위치
    vector<vector<int>> key={{3,1}, {0,0}, {0,1}, {0,2}, {1,0}, {1,1}, {1,2}, {2,0}, {2,1}, {2,2}, {3,0}, {3,2}};
    // 왼손과 오른손은 각각 *과 #의 위치에서 출발
    int left = 10;
    int right = 11;

    for(int i = 0; i<numbers.size(); i++){
        // 1, 4, 7 인 경우 왼손이 클릭
        if(numbers[i] % 3 == 1){
            answer += 'L';
            left = numbers[i];
        }
        // 3, 6, 9 인 경우 왼손이 클릭
        else if(numbers[i] % 3 == 0 && numbers[i] != 0){
            answer += 'R';
            right = numbers[i];
        }
        // 0, 2, 5, 8 인 경우
        else{
            // 왼손과 오른손이 다음 숫자 위치로부터 떨어진 거리 계산
            int left_dis = abs(key[numbers[i]][0] - key[left][0]) + abs(key[numbers[i]][1] - key[left][1]);
            int right_dis = abs(key[numbers[i]][0] - key[right][0]) + abs(key[numbers[i]][1] - key[right][1]);
            
            // 왼손이 더 가까우면 왼손이 클릭
            if(left_dis < right_dis){
                answer += 'L';
                left = numbers[i];
            }
            // 오른손이 더 가까우면 오른손이 클릭
            else if(right_dis < left_dis){
                answer += 'R';
                right = numbers[i];
            }
            // 거리가 같으면 hand의 유형에 따라 클릭
            else{
                // hand가 왼손이면 왼손이 클릭
                if(hand == "left"){
                    answer += 'L';
                    left = numbers[i];
                }
                // hand가 오른손이면 오른손이 클릭
                else{
                    answer += 'R';
                    right = numbers[i];
                }
            }
        }
    }
    return answer;
}

int main(){
    cout << solution({1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5}, "right") << endl;
    cout << solution({7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2}, "left") << endl;
    cout << solution({1, 2, 3, 4, 5, 6, 7, 8, 9, 0}, "right") << endl;
}