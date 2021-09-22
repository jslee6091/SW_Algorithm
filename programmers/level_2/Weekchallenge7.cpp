#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// enter 순서대로 회의실 입장하고 leave 순서대로 퇴장할 때 반드시 만나는 사람 구하기
vector<int> solution(vector<int> enter, vector<int> leave) {
    vector<int> answer(enter.size());
    vector<int> room;
    int entering = 0;
    int leaving = 0;

    while(leaving < leave.size()){
        // 현재 퇴장해야하는 사람이 회의실에 없을 때 회의실 입장
        if(find(room.begin(), room.end(), leave[leaving]) == room.end()){
            room.push_back(enter[entering]);
            entering++;
        }
        // 퇴장해야하는 사람이 있으면 회의실에서 만난 사람수를 더한 후 퇴장
        else{
            room.erase(find(room.begin(), room.end(), leave[leaving]));
            for(int i = 0; i < room.size(); i++){
                answer[leave[leaving] - 1]++;
                answer[room[i] - 1]++;
            }
            leaving++;
        }
    }

    return answer;
}

int main(){
    vector<int> result1 = solution({1,3,2}, {1,2,3});
    vector<int> result2 = solution({1,4,2,3}, {2,1,3,4});
    vector<int> result3 = solution({3,2,1}, {2,1,3});
    
    for(int num : result1){
        cout << num << " ";
    }
    cout << endl;

    for(int num : result2){
        cout << num << " ";
    }
    cout << endl;

    for(int num : result3){
        cout << num << " ";
    }
    cout << endl;
    return 0;
}