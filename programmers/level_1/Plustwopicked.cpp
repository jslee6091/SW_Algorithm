#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

// 나의 풀이
vector<int> solution1(vector<int> &numbers) {
    vector<int> answer;
    for (int i = 0; i< numbers.size(); i++){
        for (int j = 1; j<numbers.size() - i; j++){
            answer.push_back(numbers[i] + numbers[i+j]);
        }
    }
    sort(answer.begin(), answer.end());
    answer.erase(unique(answer.begin(), answer.end()), answer.end());
    return answer;
}

// 다른 사람의 풀이(set 이용)
vector<int> solution2(vector<int> numbers) {
    vector<int> answer;
    set<int> num;
    for (int i = 0; i< numbers.size(); i++){
        for (int j = 1; j<numbers.size() - i; j++){
            num.insert(numbers[i] + numbers[i+j]);
        }
    }
    answer.assign(num.begin(), num.end());
    return answer;
}

int main(){
    vector<int> inputs = {1,4,7,22,43};
    vector<int> output1 = solution1(inputs);
    for (int i = 0; i<output1.size(); i++){
        cout << output1[i] << " ";
    }
    cout << endl;
    // printf("set 이용\n");
    cout << "set" << endl;

    vector<int> output2 = solution2(inputs);
    for (int i = 0; i<output1.size(); i++){
        cout << output2[i] << " ";
    }
    cout << endl;

    return 0;
    
}