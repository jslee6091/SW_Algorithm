#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    map<int, int> table;

    int number = 0;
    int zero = 0;

    table.insert(pair<int, int>(6,1));
    table.insert(pair<int, int>(5,2));
    table.insert(pair<int, int>(4,3));
    table.insert(pair<int, int>(3,4));
    table.insert(pair<int, int>(2,5));
    table.insert(pair<int, int>(1,6));
    table.insert(pair<int, int>(0,6));

    for(auto num : lottos){
        auto temp = find(win_nums.begin(), win_nums.end(), num);
        if(temp != win_nums.end()){
            number++;
        }

        if(num == 0){
            zero++;
        }
    }
    answer.push_back(table[number + zero]);
    answer.push_back(table[number]);
    return answer;
}

int main(){
    vector<int> result1 = solution({44,1,0,0,31,25}, {31,10,45,1,6,19});
    cout << "result :";
    for(auto num : result1){
        cout << num << " ";
    }
    cout << endl;
}