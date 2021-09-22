#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    int start = 0;
    int end = people.size() - 1;
    
    int *visit = new int[people.size()]{};
    sort(people.begin(), people.end());

    // vector의 시작과 끝에서 동시에 출발하여 limit 이하를 만족하는 최소 구명보트 수 찾기
    while(start <= end){
        if(people[start] + people[end] <= limit){
            start++;
            end--;
        }
        else{
            end--;
        }
        answer++;
    }

    /* 처음에 만든 코드
        : 작은 수부터 시작하여 더한 값이 limit 이하를 만족하는 가장 큰 수를 찾기
        : 정확성은 좋으나 시간초과 발생
    
    int number = 0;
    int index = 0;

    while(number < people.size()){
        if(visit[index] == 1){
            index++;
            continue;
        }

        int secondidx = 0;
        for(int i = people.size() - 1; i > index; i--){
            if(people[index] + people[i] <= limit && visit[i] == 0){
                secondidx = i;
                break;
            }
        }
        visit[index] = 1;
        number++;

        if(secondidx != 0){
            visit[secondidx] = 1;
            number++;
        }

        index++;
        answer++;
    }
    */
    
    return answer;
}

int main(){
    cout << solution({70,50,80,50}, 100) << endl;
    cout << solution({70,80,50}, 100) << endl;
    return 0;
}