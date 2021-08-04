#include <vector>
#include <iostream>
#include <queue>
#include <string.h>

using namespace std;

bool visit[100][100];
int dx[4] = {0, -1, 0, 1};
int dy[4] = {1, 0, -1, 0};
int mm, nn;

int dfs(vector<vector<int>>picture, int i, int j, int value){
    visit[i][j] = true;
    int size = 1;

    for(int k = 0; k<4; k++){
        int nx = j + dx[k];
        int ny = i + dy[k];

        if(nx >= nn || ny >= mm || nx < 0 || ny < 0 || visit[ny][nx]){
            continue;
        }

        if(picture[ny][nx] != value){
            continue;
        }

        size += dfs(picture, ny, nx, value);
    }

    return size;
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size = 0;
    mm = m;
    nn = n;

    vector<int> answer(2);

    memset(visit, 0, sizeof(visit));

    for(int i = 0; i<picture.size(); i++){
        for(int j = 0; j<picture[i].size(); j++){
            if(!visit[i][j] && picture[i][j] != 0){
                number_of_area++;
                max_size = max(max_size, dfs(picture, i, j, picture[i][j]));
            }
        }
    }
    answer[0] = number_of_area;
    answer[1] = max_size;
    return answer;
}

int main(){
    vector<int> result = solution(6, 4, {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}});
    for(auto num : result){
        cout << num << " ";
    }
    cout << endl;
}