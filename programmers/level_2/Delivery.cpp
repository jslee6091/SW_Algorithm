#include <iostream>
#include <vector>
#include <limits>

using namespace std;

// Dijkstra algorithm을 활용한 최단 경로 찾기
int find_min(vector<int> dist, int *visits){
    // 남은 지점들 중 distance 값이 가장 작은 요소의 인덱스 구하는 함수
    int minimum = numeric_limits<int>::max();
    int min_index = 0;

    for(int i = 0; i < dist.size(); i++){
        if(visits[i] == 0 && minimum > dist[i]){
            minimum = dist[i];
            min_index = i;
        }
    }

    return min_index;
}

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 1;

    int *visit = new int[N]{};

    vector<int> distance(N);
    for(int i = 1; i < N; i++){
        distance[i] = numeric_limits<int>::max();
    }

    int count = 0;
    int num = 0;

    // dijkstra algorithm
    while(count < N - 1){
        // 주어진 도로 정보에 대한 경로 탐색
        for(int i = 0; i < road.size(); i++){
            if(road[i][0] - 1 == num){
                // 현재 지점의 distance 값과 목적지 사이의 거리를 더하기
                int temp = distance[num] + road[i][2];
                // 목적지의 distance 값보다 작은 경우 최단 경로이므로 변경
                if(temp < distance[road[i][1] - 1]){
                    distance[road[i][1] - 1] = temp;
                }
            }
            else if(road[i][1] - 1 == num){
                int temp = distance[num] + road[i][2];
                if(temp < distance[road[i][0] - 1]){
                    distance[road[i][0] - 1] = temp;
                }
            }
        }

        // 현재 지점 방문 표시
        visit[num] = 1;
        // 남은 지점들 중 distance 값이 최소인 요소의 인덱스 구하기
        num = find_min(distance, visit);
        count++;
    }

    for(int i = 1; i < N; i++){
        if(distance[i] <= K){
            answer++;
        }
    }
    return answer;
}

int main(){
    cout << solution(5, {{1,2,1},{2,3,3},{5,2,2},{1,4,2},{5,3,1},{5,4,2}}, 3) << endl;
    cout << solution(6, {{1,2,1},{1,3,2},{2,3,2},{3,4,3},{3,5,2},{3,5,3},{5,6,1}}, 4) << endl;
    return 0;
}