#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

int isPrime(int num);

int solution(vector<int> nums) {
    int answer = 0;

    for(int i = 0; i<nums.size(); i++){
        for(int j = i + 1; j<nums.size(); j++){
            for(int k = j + 1; k<nums.size(); k++){
                if(isPrime(nums[i] + nums[j] + nums[k])){
                    answer++;
                }
            }
        }
    }
    return answer;
}

int isPrime(int num){
    for(int i = 2; i<= pow(num, 0.5); i++){
        if(num % i == 0){
            return 0;
        }
    }
    return 1;
}

int main(){
    cout << solution({1,2,3,4}) << endl;
    cout << solution({1,2,7,6,4}) << endl;
}