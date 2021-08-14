#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

int bfs(vector<string> place, queue<tuple<int, int, int>> waits){

    int move[4][2] = {{0,1}, {0,-1}, {-1,0}, {1,0}};
    int is_visited[5][5] = {0};

    while(waits.size() > 0){
        // queue의 맨 앞의 원소를 저장 후 삭제
        tuple<int, int, int> temp = waits.front();
        waits.pop();

        // tuple 값 저장
        int row = get<0>(temp);
        int col = get<1>(temp);
        int count = get<2>(temp);
        
        // 맨 처음 탐색 시작할 때를 위한 방문 표시
        is_visited[row][col] = 1;

        // 이동거리가 2인 경우
        if(count == 2){
            // 방문하지 않았고 P 인 경우 0 return
            if(place[row][col] == 'P' && is_visited[row][col] == 0){
                return 0;
            }
            continue;
        }

        // 너비 우선 탐색
        for(int i = 0; i<4; i++){
            int new_row = row + move[i][0];
            int new_col = col + move[i][1];

            // 다음 위치가 범위를 벗어난 경우 pass
            if(new_row >= 5 || new_row < 0 || new_col >= 5 || new_col < 0){
                continue;
            }

            // 다음 위치가 방문하지 않았고 O 인 경우 큐에 저장, 방문했음을 표시
            if(place[new_row][new_col] == 'O' && is_visited[new_row][new_col] == 0){
                waits.push(make_tuple(new_row, new_col, count + 1));
                is_visited[new_row][new_col] = 1;
            }
            // 다음 위치가 방문하지 않았고 P 인 경우 거리가 2 이하이므로 0 return
            else if(place[new_row][new_col] == 'P' && is_visited[new_row][new_col] == 0){
                return 0;
            }
        }
    }
    return 1;
}

// 2차원 벡터 places의 요소들 중 P 사이의 거리가 2이하인 경우를 찾아내는 문제
vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    queue<tuple<int, int, int>> wait;

    for(int i = 0; i < 5; i++){
        int is_True = 0;
        for(int j = 0; j < 5; j++){
            // string 문자열 각각의 문자에 대한 조회
            for(int k = 0; k < 5; k++){
                if(places[i][j][k] == 'P'){
                    wait.push(make_tuple(j,k,0));
                    if (bfs(places[i], wait) == 0){
                        answer.push_back(0);
                        // 0이 반환되면 바로 중단
                        is_True = 1;
                        break;
                    }
                }
            }

            // 탐색 결과가 0이 나온 경우 탐색 중단
            if(is_True){
                break;
            }
        }

        // 0이 나오지 않은 경우 정답에 1 추가
        if(is_True == 0){
            answer.push_back(1);
        }

        // 다음 탐색을 위해 queue 비우기
        while(!wait.empty()){
            wait.pop();
        }
    }

    return answer;
}

int main(){
    vector<int> result = solution({{"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"},
                                    {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"},
                                    {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"},
                                    {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"},
                                    {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}});
    
    for(int num : result){
        cout << num;
    }
    cout << endl;

    return 0;        
}