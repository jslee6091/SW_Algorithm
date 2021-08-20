// Reference : https://ansohxxn.github.io/programmers/82/
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iostream>

using namespace std;

// 조합을 이용하는 문제

// 내림차순 정렬을 위한 함수
bool cmp(pair<string, int> a, pair<string, int> b){
    return a.second > b.second;
}

// 모든 조합에 대한 탐색 실행
void DFS(map<string, int>& dic, string& order, string comb, int index, int depth) {
    // course개의 문자를 뽑은 경우 map에 저장 후 return
    if(depth == comb.length()){
        dic[comb]++;
        return;
    }

    // order 문자열에서 course개의 문자를 뽑는 조합
    for(int i=index;i<order.length();i++){
        comb[depth] = order[i];
        DFS(dic, order, comb, i + 1, depth + 1);
    }
}

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    map<string, int> dic;
    
    // order의 요소들에 대해 탐색
    for(int i=0;i<orders.size();i++){
        // 문자열 정렬
        sort(orders[i].begin(),orders[i].end());
        // 새로 구성하는 메뉴의 개수인 course의 원소에 대한 탐색
        for(int j=0;j<course.size();j++){
            string comb = "";
            // course 원소 크기의 문자열 생성
            comb.resize(course[j]);
            DFS(dic,orders[i],comb,0,0); 
        }
    }
    vector<pair<string,int>> sorted;
    for (auto& order : dic){
        // 특정 조합의 메뉴가 2개 이상인 경우 sorted에 저장
        if (order.second > 1){
            sorted.push_back(make_pair(order.first, order.second));
        }
    }
    // 개수가 많은 조합 순서대로 정렬
    sort(sorted.begin(), sorted.end(), cmp);
    
    // course개의 메뉴 중 가장 많은 메뉴 조합을 정답으로 선정
    for(int i = 0; i < course.size(); i++){
        int max = 0;
        // 모든 sorted에 대해
        for(int j = 0; j < sorted.size(); j++){
            // 메뉴 문자열의 크기가 course값과 다르면 continue
            if (sorted[j].first.length() != course[i]) continue;
            // 메뉴 문자열의 크기가 course값과 같고 max = 0 이면(처음으로 추가할 때)
            else if (max == 0){
                // sorted를 내림차순으로 정렬했으므로 바로 정답에 추가
                answer.push_back(sorted[j].first);
                // 메뉴의 개수를 max에 저장
                max = sorted[j].second;
            }
            // 메뉴 조합의 개수가 이전의 max값과 같을때(최대개수가 같은 메뉴 조합이 여러개인 경우)
            else if (max == sorted[j].second) {
                // 정답에 추가
                answer.push_back(sorted[j].first);
            }
            else break;
        }
    }

    // 정답을 오름차순으로 정렬
    sort(answer.begin(), answer.end());
    return answer;
}

int main(){
    vector<string> result = solution({"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"}, {2,3,4});
    
    cout << "========= result ========" << endl;
    for(string str : result){
        cout << str << " ";
    }
    cout << endl;

    vector<string> result2 = solution({"ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"}, {2,3,5});
    
    cout << "========= result2 ========" << endl;
    for(string str : result2){
        cout << str << " ";
    }
    cout << endl;

    vector<string> result3 = solution({"XYZ", "XWY", "WXA"}, {2,3,4});
    
    cout << "========= result3 ========" << endl;
    for(string str : result3){
        cout << str << " ";
    }
    cout << endl;

}