#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string lists[10] = {"java", "python", "cpp", "backend", "frontend", "junior", "senior", "chicken", "pizza", "-"};

vector<int> solution(vector<string> info, vector<string> query) {
    vector<int> answer;
    int index = 0;
    
    for(int i = 0; i < query.size(); i++){
        int *match = new int[info.size()]{};
        
        for(int j = 0; j < 8; j++){
            int blank = query[i].find(" ");
            string s = query[i].substr(0, blank);
            query[i] = query[i].substr(blank + 1);
            
            if(s == "-" or s == "and"){
                continue;
            }
            
            if(!count(lists, lists + 10, s)){
                for(int k = 0; k < info.size(); k++){
                    int infoNum = atoi(info[k].substr(info[k].rfind(" ") + 1).c_str());
                    int queNum = atoi(s.c_str());
                    
                    if(infoNum < queNum){
                       match[k] = 1;
                    }
                }
                
                continue;
            }
            
            for(int k = 0; k < info.size(); k++){
                if(info[k].find(s) == string :: npos){
                    match[k] = 1;
                }
            }
        }
        
        answer.push_back(count(match, match + info.size(), 0));
    }
    
    return answer;
}

int main(){
    vector<int> result = solution({"java backend junior pizza 150",
                                    "python frontend senior chicken 210",
                                    "python frontend senior chicken 150",
                                    "cpp backend senior pizza 260",
                                    "java backend junior chicken 80",
                                    "python backend senior chicken 50"},
                                    {"java and backend and junior and pizza 100",
                                    "python and frontend and senior and chicken 200",
                                    "cpp and - and senior and pizza 250",
                                    "- and backend and senior and - 150",
                                    "- and - and - and chicken 100",
                                    "- and - and - and - 150"});
    
    for(int num : result){
        cout << num << " ";
    }
    cout << endl;
}