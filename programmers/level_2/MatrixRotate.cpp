#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    vector<vector<int>> array;
    vector<int> initialize;
    queue<int> que;

    // initialize the array
    for(int i = 0; i< rows; i++){
        array.push_back(initialize);
        for(int j = 0; j< columns; j++){
            array[i].push_back(i * columns + j + 1);
        }
    }

    for(vector<int> quer : queries){

        int row_start = quer[0] - 1;
        int row_end = quer[2] - 1;
        int col_start = quer[1] - 1;
        int col_end = quer[3] - 1;

        // initialize queue and minimun value
        que.push(array[row_start][col_start]);
        int min = array[row_start][col_start];

        // go right
        for(int i = col_start; i < col_end; i++){
            que.push(array[row_start][i + 1]);

            // check minimun value
            if(min > array[row_start][i + 1]){
                min = array[row_start][i + 1];
            }

            array[row_start][i + 1] = que.front();
            que.pop();
        }

        // go down
        for(int i = row_start; i < row_end; i++){
            que.push(array[i + 1][col_end]);

            // check minimun value
            if(min > array[i + 1][col_end]){
                min = array[i + 1][col_end];
            }

            array[i + 1][col_end] = que.front();
            que.pop();
        }

        // go left
        for(int i = col_end; i > col_start; i--){
            que.push(array[row_end][i - 1]);

            // check minimun value
            if(min > array[row_end][i - 1]){
                min = array[row_end][i - 1];
            }

            array[row_end][i - 1] = que.front();
            que.pop();
        }

        // go up
        for(int i = row_end; i > row_start; i--){
            que.push(array[i - 1][col_start]);

            // check minimun value
            if(min > array[i - 1][col_start]){
                min = array[i - 1][col_start];
            }

            array[i - 1][col_start] = que.front();
            que.pop();
        }

        answer.push_back(min);

        // clear queue
        while(!que.empty()){
            que.pop();
        }

    }
    return answer;
}

int main(){
    vector<int> result1 = solution(6, 6, {{2,2,5,4},{3,3,6,6},{5,1,6,3}});
    vector<int> result2 = solution(3, 3, {{1,1,2,2},{1,2,2,3},{2,1,3,2},{2,2,3,3}});
    vector<int> result3 = solution(100, 97, {{1,1,100,97}});
    
    for(int num : result1) cout << num << " ";
    cout << endl;
    for(int num : result2) cout << num << " ";
    cout << endl;
    for(int num : result3) cout << num << " ";
    cout << endl;
    
}