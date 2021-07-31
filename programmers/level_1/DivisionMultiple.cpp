#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int solution(int left, int right) {
    int answer = 0;
    for(int i = left; i<=right; i++){
        float square = sqrt(i);
        if(square - static_cast<int>(square) != 0){
            answer += i;
        }
        else{
            answer -= i;
        }
    }
    return answer;
}

int main(){
    cout << solution(13, 17) << endl;
    cout << solution(24, 27) << endl;
}