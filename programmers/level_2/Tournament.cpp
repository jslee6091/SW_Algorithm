#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

// 번호 순서대로 토너먼트 대진표를 받을 때 a와 b가 만나는 라운드 수를 구하기
int solution(int n, int a, int b)
{
    int answer = 0;

    /* Method using queue - 시간 초과 발생
    queue<int> que;

    for(int i = 0; i < n; i++){
        que.push(i + 1);
    }

    int rounds = 1;
    while(!que.empty()){
        int matches = que.size() / 2;
        for(int j = 0; j < matches; j++){
            int player1 = que.front();
            que.pop();
            int player2 = que.front();
            que.pop();
            if(player1 == a && player2 == b || player1 == b && player2 == a){
                answer = rounds;
                break;
            }
            else if(player1 == a || player1 == b){
                que.push(player1);
            }
            else{
                que.push(player2);
            }
        }
        rounds++;
    }
    */

    int rounds = log(n) / log(2);
    
    while(true){
        int middle = n / 2;
        if(a <= middle && b <= middle or a > middle && b > middle){
            rounds--;
            n = n / 2;
            if(a > middle && b > middle){
                a -= middle;
                b -= middle;
            }
            continue;
        }
        else{
            answer = rounds;
            break;
        }
    }

    return answer;
}

int main(){
    cout << solution(8, 4, 7) << endl;
    return 0;
}