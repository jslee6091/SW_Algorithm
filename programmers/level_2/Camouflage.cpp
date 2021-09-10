#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

// clothes 중 서로 다른 종류의 옷을 최소 한벌 이상 입는 경우의 수 구하기
int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> mp;
    map<string, int>::iterator iter;

    // 각 종류별 옷의 개수를 map에 저장
    for(int i = 0; i < clothes.size(); i++){
        // map의 key가 이미 있으면 value를 1증가
        if(mp.find(clothes[i][1]) != mp.end()){
            mp[clothes[i][1]]++;
        }
        // key가 없으면 새로 삽입 후 value를 1로 초기화
        else{
            mp[clothes[i][1]] = 1;
            // mp.insert(pair<string, int>(clothes[i][1], 1));
            // mp.insert({clothes[i][1], 1});
        }
    }

    // 옷을 입는 경우의 수는 각 종류별 옷 개수에 1씩 더한 값을 곱한 후 1 빼기
    for(iter=mp.begin(); iter!=mp.end(); iter++){
        answer *= iter->second + 1;
    }
    // 아무것도 입지 않은 경우 하나를 제거
    answer -= 1;

    /*
        처음에는 각 옷을 선택하는 모든 경우의 수를 조합을 이용해 구했지만
        시간초과가 발생하여 인터넷을 찾아본 결과 각 경우의 수를 곱셈하면
        된다는 것을 알게됨
    */
   
    return answer;
}

int main(){
    cout << solution({{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}}) << endl;
    cout << solution({{"crowmask", "face"}, {"bluesunglasses", "face"}, {"smoky_makeup", "face"}}) << endl;
    cout << solution({{"don", "face"}, {"eee", "face"}, {"hello", "sang"}, {"nice", "ha"}, {"welcome", "gut"}}) << endl;
    return 0;
}