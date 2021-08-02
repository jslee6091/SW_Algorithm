#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

// 최소 힙을 이용한 문제
int solution(vector<int> scoville, int K) {
    int answer = 0;
    
    // 최소 힙 구현을 위해 priority_queue를 사용
    priority_queue<int, vector<int>, greater<int>> prq;
    // scoville 값들을 모두 priority_queue에 삽입
    for(int num : scoville){
        prq.push(num);
    }
    
    // 최소 힙의 루트 노드 값(가장 작은 값)이 K 보다 작은 경우
    while(prq.top() < K && prq.size() > 1){
        // 가장 작은 두 값을 꺼내서 연산 후 다시 삽입
        int first = prq.top();
        prq.pop();
        int second = prq.top();
        prq.pop();
        prq.push(first + second * 2);
        // 연산 횟수 1 증가
        answer++;
    }
    
    // 최소 힙의 모든 요소들을 탐색했음에도 여전히 K 보다 작으면 -1 return
    if(prq.top() < K){
        answer = -1;
    }
    
    return answer;
}

int main(){
    cout << solution({1, 2, 3, 9, 10, 12}, 7) << endl;
    return 0;
}