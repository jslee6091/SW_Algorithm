#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

// 숫자를 2진법으로 바꾼 후 이 숫자보다 큰 수 중 다른 비트가 2이하인 최소값 구하기
vector<long long> solution(vector<long long> numbers) {
    vector<long long> answer;

    // 1의 자리수부터 n개의 1이 연속으로 있을 때 2^(n-1) 만큼 더한 값이 정답
    for(int i = 0; i < numbers.size(); i++){
        // 짝수는 항상 1의 자리가 0이므로 바로 정답 삽입
        if(numbers[i] % 2 == 0){
            answer.push_back(numbers[i] + 1);
            continue;
        }

        // 홀수인 경우 1의 개수를 구한 후 정답 삽입
        long long temp = numbers[i];
        int sq = -1;
        while(temp != 0){
            if(temp % 2 == 1){
                sq++;
                temp /= 2;
            }
            else{
                break;
            }
        }
        answer.push_back(numbers[i] + pow(2, sq));

        /* 아래 코드는 처음에 무식한(?) 방법으로 구했는데 정확도는 좋았으나 시간 초과 발생
        // make binary number
        string stnum = "";
        long long num = numbers[i];
        while(num != 0){
            stnum.insert(0, to_string(num % 2));
            num /= 2;
        }


        // get answer
        long long count = 1;
        string temp = stnum;

        while(true){
            int pluses = 0;
            int carry = 0;

            // add 1
            for(int j = temp.size() - 1; j >= 0; j--){
                if(j == temp.size() - 1){
                    if(temp[j] == '0'){
                        temp[j] = '1';
                    }
                    else{
                        temp[j] = '0';
                        carry = 1;
                    }
                }
                else if(carry){
                    if(temp[j] == '1'){
                        temp[j] = '0';
                    }
                    else{
                        temp[j] = '1';
                        carry = 0;
                    }
                }

                if(temp[j] != stnum[j]){
                    pluses++;
                }
            }

            if(carry){
                temp.insert(0, "1");
                stnum.insert(0, "0");
                pluses++;
            }

            if(pluses < 3){
                answer.push_back(numbers[i] + count);
                break;
            }
            else{
                count++;
            }
        }
        */
    }

    return answer;
}

int main(){
    vector<long long> result = solution({2, 7});
    for(long long nn : result){
        cout << nn << " ";
    }
    cout << endl;
    return 0;
}