#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <locale>

using namespace std;

// 페이지 교체 알고리즘인 LRU(Least Recently Used)를 구현하는 문제
int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    vector<string> cache;
    locale loc;

    // cache 크기가 0이면 무조건 5 * 데이터 크기
    if(cacheSize == 0){
        answer = cities.size() * 5;
    }
    else{
        for(int i = 0; i < cities.size(); i++){
            string temp = "";
            // 대문자를 소문자로 바꾸기
            for(int j = 0; j < cities[i].length(); j++){
                temp += tolower(cities[i][j], loc);
            }

            // cache에 데이터가 없는 경우
            if(find(cache.begin(), cache.end(), temp) == cache.end()){
                answer += 5;
                // cache의 크기가 cacheSize이상인 경우 가장 오래된 데이터 삭제
                if(cache.size() >= cacheSize){
                    cache.erase(cache.begin());
                }
            }
            // cache에 데이터가 있는 경우
            else{
                answer += 1;
                cache.erase(find(cache.begin(), cache.end(), temp));
            }
            cache.push_back(temp);
        }
    }
    return answer;
}

int main(){
    cout << solution(3, {"Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"}) << endl;
    cout << solution(3, {"Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"}) << endl;
    cout << solution(2, {"Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"}) << endl;
    cout << solution(5, {"Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"}) << endl;
    cout << solution(2, {"Jeju", "Pangyo", "NewYork", "newyork"}) << endl;
    cout << solution(0, {"Jeju", "Pangyo", "Seoul", "NewYork", "LA"}) << endl;
    return 0;
}