#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

// 0과 1로 이루어진 2^n * 2^n 크기의 배열을 쿼드 트리 방식으로 압축하는 문제
// 전체 원소가 모두 같지 않으면 정확히 4구역으로 나누어 각각의 구역에서 탐색을 반복
vector<int> get_zip(vector<vector<int>> array, int startrow, int endrow, int startcol, int endcol){
    int num = array[startrow][startcol];
    vector<int> ans = {0, 0};
    bool iszip = true;

    if(endrow - startrow != 1){
        for(int i = startrow; i < endrow; i++){
            for(int j = startcol; j < endcol; j++){
                if(array[i][j] != num){
                    iszip = false;
                    int middlerow = (startrow + endrow) / 2;
                    int middlecol = (startcol + endcol) / 2;
                    vector<int> result;

                    if(middlerow - startrow == 1){
                        ans[array[startrow][startcol]]++;
                    }
                    else{
                        result = get_zip(array, startrow, middlerow, startcol, middlecol);
                        ans[0] += result[0];
                        ans[1] += result[1];
                    }

                    if(endrow - middlerow == 1){
                        ans[array[middlerow][startcol]]++;
                    }
                    else{
                        result = get_zip(array, middlerow, endrow, startcol, middlecol);
                        ans[0] += result[0];
                        ans[1] += result[1];
                    }

                    if(middlerow - startrow == 1){
                        ans[array[startrow][middlecol]]++;
                    }
                    else{
                        result = get_zip(array, startrow, middlerow, middlecol, endcol);
                        ans[0] += result[0];
                        ans[1] += result[1];
                    }

                    if(endrow - middlerow == 1){
                        ans[array[middlerow][middlecol]]++;
                    }
                    else{
                        result = get_zip(array, middlerow, endrow, middlecol, endcol);
                        ans[0] += result[0];
                        ans[1] += result[1];
                    }

                    break;
                }
            }

            if(!iszip){
                break;
            }
        }
    }

    if(iszip){
        ans[num]++;
    }

    return ans;
}

// 재귀를 이용한 구현 : 정확성은 높았으나 시간초과가 발생
vector<int> solution_recursive(vector<vector<int>> arr){
    vector<int> answer;
    answer = get_zip(arr,0,arr.size(),0,arr[0].size());
    return answer;
}

// Queue를 이용한 구현 : 정확성이 높고 실행 속도가 재귀에 비해 매우 높았다.
vector<int> solution(vector<vector<int>> arr) {
    vector<int> answer = {0, 0};
    
    int num = arr.size();
    queue<pair<pair<int,int>, pair<int, int>>> que;
    que.push(make_pair(make_pair(0, num), make_pair(0, num)));

    while(!que.empty()){
        pair<pair<int,int>, pair<int, int>>temp = que.front();
        que.pop();

        int n = arr[temp.first.first][temp.second.first];
        bool issame = true;

        for(int i = temp.first.first; i < temp.first.second; i++){
            for(int j = temp.second.first; j < temp.second.second; j++){
                if(arr[i][j] != n){
                    issame = false;
                    int middlerow = (temp.first.first + temp.first.second) / 2;
                    int middlecol = (temp.second.first + temp.second.second) / 2;
                    que.push(make_pair(make_pair(temp.first.first, middlerow), make_pair(temp.second.first, middlecol)));

                    que.push(make_pair(make_pair(middlerow, temp.first.second) , make_pair(temp.second.first, middlecol)));

                    que.push(make_pair(make_pair(temp.first.first, middlerow), make_pair(middlecol, temp.second.second)));

                    que.push(make_pair(make_pair(middlerow, temp.first.second), make_pair(middlecol, temp.second.second)));
                    break;
                }
            }

            if(!issame){
                break;
            }
        }

        if(issame){
            answer[n]++;
        }
    }

    return answer;
}

int main(){
    vector<int> result = solution({{1,1,0,0},{1,0,0,0},{1,0,0,1},{1,1,1,1}});
    vector<int> result2 = solution({{1,1,1,1,1,1,1,1},{0,1,1,1,1,1,1,1},{0,0,0,0,1,1,1,1},{0,1,0,0,1,1,1,1},{0,0,0,0,0,0,1,1},{0,0,0,0,0,0,0,1},{0,0,0,0,1,0,0,1},{0,0,0,0,1,1,1,1}});

    for(int nn : result){
        cout << nn << " ";
    }
    cout << endl;

    for(int nn : result2){
        cout << nn << " ";
    }
    cout << endl;

}