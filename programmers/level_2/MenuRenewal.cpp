// Reference : https://ansohxxn.github.io/programmers/82/
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iostream>

using namespace std;

bool cmp(pair<string, int> a, pair<string, int> b){
    return a.second > b.second;
}

void DFS(map<string, int>& dic, string& order, string comb, int index, int depth) {
    if(depth == comb.length()){
        dic[comb]++;
        return;
    }

    for(int i=index;i<order.length();i++){
        comb[depth] = order[i];
        DFS(dic, order, comb, i + 1, depth + 1);
    }
}

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    map<string, int> dic;
    for(int i=0;i<orders.size();i++){
        sort(orders[i].begin(),orders[i].end());
        for(int j=0;j<course.size();j++){
            string comb = "";
            comb.resize(course[j]);
            DFS(dic,orders[i],comb,0,0); 
        }
    }
    vector<pair<string,int>> sorted;
    for (auto& order : dic){
        if (order.second > 1){
            sorted.push_back(make_pair(order.first, order.second));
        }
    }
    sort(sorted.begin(), sorted.end(), cmp);
    for(int i = 0; i < course.size(); i++){
        int max = 0;
        for(int j = 0; j < sorted.size(); j++){
            if (sorted[j].first.length() != course[i]) continue;
            else if (max == 0){
                answer.push_back(sorted[j].first);
                max = sorted[j].second;
            }
            else if (max == sorted[j].second) answer.push_back(sorted[j].first);
            else break;
        }
    }
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