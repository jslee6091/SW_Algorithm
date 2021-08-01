#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int answer = 0;

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

int solution1(vector<int> numbers, int target) {
    target_dfs(numbers, 0, 0, target);
    return answer;
}

int solution2(vector<int> numbers, int target){
    queue<int> que;
    int count = 0;
    que.push(0);
    
    while(count < numbers.size()){
        int temp = 0;
        while(temp < 1 << count){
            int temp2 = que.front();
            que.pop();

            que.push(temp2 + numbers[count]);
            que.push(temp2 - numbers[count]);
            temp++;
        }
        count++;
    }

}

int main(){
    cout << solution1({1,1,1,1,1}, 3) << endl;

}