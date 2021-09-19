#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    stack<pair<int, int>> stk;

    while(true){
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(i + 1 >= m || j + 1 >= n){
                    continue;
                }

                if(board[i][j] == '-'){
                    continue;
                }

                if(board[i][j] == board[i + 1][j] && board[i][j] == board[i][j + 1] && board[i][j] == board[i + 1][j + 1]){
                    stk.push(make_pair(i, j));
                    stk.push(make_pair(i, j + 1));
                    stk.push(make_pair(i + 1, j));
                    stk.push(make_pair(i + 1, j + 1));
                }
            }
        }

        if(stk.empty()){
            break;
        }

        while(!stk.empty()){
            pair<int, int> temp = stk.top();
            stk.pop();
            if(board[temp.first][temp.second] == '-'){
                continue;
            }
            else{
                board[temp.first][temp.second] = '-';
                answer++;
            }
        }

        for(int j = 0; j < n; j++){
            for(int i = 1; i < m; i++){
                if(board[i][j] == '-'){
                    int start = i;
                    while(start > 0){
                        board[start][j] = board[start - 1][j];
                        board[start - 1][j] = '-';
                        start--;
                    }
                }
            }
        }
    }

    return answer;
}

int main(){
    cout << solution(4, 5, {"CCBDE", "AAADE", "AAABF", "CCBBF"}) << endl;
    cout << solution(6, 6, {"TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"}) << endl;
    cout << solution(5, 5, {"11223", "11324", "23324", "33311", "33211"}) << endl;
    return 0;
}