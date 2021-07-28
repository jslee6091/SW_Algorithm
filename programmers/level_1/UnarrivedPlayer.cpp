#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;

// vector 정렬을 이용한 풀이
string solution1(vector<string> participant, vector<string> completion) {
    string answer = "";

    // participant와 completion의 요소들 알파벳 순서로 정렬
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    // completion.push_back(" ");

    // participant에 대응하는 completion 요소가 다른 경우 정답 
    for(int i = 0; i < participant.size(); i++){
        if(participant[i] != completion[i]){
            answer = participant[i];
            break;
        }
    }

    return answer;
}

// unordered_map을 이용한 풀이 - 문제에서 의도하는 해시를 이용
string solution2(vector<string> participant, vector<string> completion){
    string answer = "";
    unordered_map<string, int> hashi;
    
    // participant의 요소들을 unordered_map에 추가
    for(string par : participant){
        hashi[par]++;
    }

    // unordered_map에서 completion 요소에 해당하는 key에 대해 value 를 1 감소
    for(string com : completion){
        hashi[com]--;
    }

    // unordered_map에서 각 key에 대한 value 가 0보다 큰 경우 정답
    for(auto num : hashi){
        if(num.second > 0){
            answer = num.first;
        }
    }

    return answer;
}

int main(){
    cout << solution1({"leo", "kiki", "eden"}, {"eden", "kiki"}) << endl;
    cout << solution1({"marina", "josipa", "nikola", "vinko", "filipa"}, {"josipa", "filipa", "marina", "nikola"}) << endl;
    cout << solution1({"mislav", "stanko", "mislav", "ana"}, {"stanko", "ana", "mislav"}) << endl;

    cout << solution2({"leo", "kiki", "eden"}, {"eden", "kiki"}) << endl;
    cout << solution2({"marina", "josipa", "nikola", "vinko", "filipa"}, {"josipa", "filipa", "marina", "nikola"}) << endl;
    cout << solution2({"mislav", "stanko", "mislav", "ana"}, {"stanko", "ana", "mislav"}) << endl;

}