#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int joystick(vector<int> distances, int index){
    int minimum = 0;
    vector<int> compare;

    for(int i = 0; i < distances.size(); i++){
        int temp = 0;
        if(distances[i]){
            temp = abs(i - index);

            if(temp >= int(distances.size() / 2) + 1){
                temp = distances.size() - temp;
            }
            distances[i] = temp;

            if(temp == 0){
                continue;
            }

            if(minimum == 0 || minimum > temp){
                minimum = temp;
            }
        }
    }

    if(minimum == 0){
        return 0;
    }

    for(int i = 0; i < distances.size(); i++){
        if(distances[i] == minimum){
            compare.push_back(minimum + joystick(distances, i));
        }
    }

    sort(compare.begin(), compare.end());
    return compare[0];
}

int solution(string name) {
    int answer = 0;
    vector<int> distances;

    for(int i = 0; i<name.size(); i++){
        int num = int(name[i]) - int('A');
        if(num >= 14){
            num = 26 - num;
        }

        distances.push_back(num);
        answer += num;
    }

    answer += joystick(distances, 0);

    return answer;
}

int main(){
    cout << solution("JEROEN") << endl;
    cout << solution("JAN") << endl;
    return 0;
}