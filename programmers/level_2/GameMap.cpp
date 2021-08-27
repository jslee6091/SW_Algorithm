#include <vector>
#include <deque>
#include <tuple>
#include <iostream>
using namespace std;

int moverow[4] = {0, 1, 0, -1};
int movecol[4] = {1, 0, -1, 0};

// BFS - 게임 맵의 시작점에서 도착점까지 갈 수 있는 최단거리 구하기
int solution(vector<vector<int>> maps)
{
    int answer = 0;
    int map_row = maps.size();
    int map_col = maps[0].size();
    
    deque<tuple<int, int, int>> dque;
    dque.push_back(make_tuple(0,0,1));
    
    while(!dque.empty()){
        tuple<int, int, int> temp = dque.front();
        dque.pop_front();
        
        int row = get<0>(temp);
        int col = get<1>(temp);
        int count = get<2>(temp);
        
        if(row == map_row - 1 && col == map_col - 1){
            return count;
        }
        
        maps[row][col] = 0;
        
        for(int i = 0; i < 4; i++){
            int nextrow = row + moverow[i];
            int nextcol = col + movecol[i];
            
            if(nextrow >= map_row || nextrow < 0 || nextcol >= map_col || nextcol < 0){
                continue;
            }
            if(maps[nextrow][nextcol] == 0){
                continue;
            }
            dque.push_back(make_tuple(nextrow, nextcol, count + 1));
        }
    }
    
    return -1;
}

int main(){
    cout << solution({{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,1},{0,0,0,0,1}}) << endl;
    cout << solution({{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,0},{0,0,0,0,1}}) << endl;
    return 0;
}

/*
    위의 내가 만든 코드는 효율성 테스트에서 시간초과가 발생하는데 아래의 코드는 그렇지 않았다.
    알고리즘과 내용이 거의 똑같은데 시간 차이가 나는 이유를 잘 모르겠다.
    아마 tuple 때문일거라 추측한다.
*/

/*
// 출처: https://yabmoons.tistory.com/480
#include<vector>
#include<queue>
using namespace std;
 
bool Visit[100][100];
 
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
 
int solution(vector<vector<int> > maps)
{
    int N = maps.size();
    int M = maps[0].size();
    queue<pair<pair<int, int>, int>> Q;
    Q.push(make_pair(make_pair(0, 0), 1));    
    Visit[0][0] = true;
    
    while(Q.empty() == 0)
    {
        int x = Q.front().first.first;
        int y = Q.front().first.second;
        int Cnt = Q.front().second;
        Q.pop();
        
        if(x == N - 1 && y == M - 1) return Cnt;
        
        for(int i = 0;  i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx >= 0 && ny >= 0 && nx < N && ny < M)
            {
                if(Visit[nx][ny] == false && maps[nx][ny] == 1)
                {
                    Visit[nx][ny] = true;
                    Q.push(make_pair(make_pair(nx, ny), Cnt + 1));
                }
            }
        }
    }
    return -1;
}
*/