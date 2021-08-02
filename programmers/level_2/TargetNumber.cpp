#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int answer = 0;

// dfs 를 이용한 풀이
void target_dfs(vector<int> num, int count, int sum, int target){
    if(count == num.size()){
        if(sum == target){
            answer++;
        }
        return;
    }

    target_dfs(num, count + 1, sum + num[count], target);
    target_dfs(num, count + 1, sum - num[count], target);
}

// dfs 함수 활용하는 solution
int solution1(vector<int> numbers, int target) {
    target_dfs(numbers, 0, 0, target);
    return answer;
}

// bfs 이용한 solution
int solution2(vector<int> numbers, int target){
    queue<int> que;
    int count = 0;
    que.push(0);
    
    // numbers의 개수만큼 실행
    while(count < numbers.size()){
        int temp = 0;

        // 원소 하나씩 조회할 수록 경우의 수가 2배씩 늘어남
        while(temp < 1 << count){
            int temp2 = que.front();
            que.pop();

            // count 값이 마지막인 경우 queue에 넣지 않고 정답 유무만 확인
            if(count == numbers.size() - 1){
                if(temp2 + numbers[count] == 3 || temp2 - numbers[count] == 3){
                    answer++;
                }
            }
            // count 값이 마지막이 아닌 경우 덧셈, 뺄셈 결과를 queue에 저장
            else{
                que.push(temp2 + numbers[count]);
                que.push(temp2 - numbers[count]);
            }
            temp++;
        }
        count++;
    }


    return answer;

}

int main(){
    cout << solution1({1,1,1,1,1}, 3) << endl;
    // 전역 변수 이므로 0으로 초기화
    answer = 0;
    cout << solution2({1,1,1,1,1}, 3) << endl;
}