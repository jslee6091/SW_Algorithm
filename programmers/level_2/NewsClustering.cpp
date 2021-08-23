#include <string>
#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

vector<string> get_multipleSet(string s){
    vector<string> answer;

    for(int i = 0; i<s.size() - 1; i++){
        if(int(s[i]) >= 97 && int(s[i]) <= 122 || int(s[i]) >= 65 && int(s[i]) <= 90){
            if(int(s[i + 1]) >= 97 && int(s[i + 1]) <= 122 || int(s[i + 1]) >= 65 && int(s[i + 1]) <= 90){
                answer.push_back(s.substr(i, 2));
            }
        }
    }
    
    return answer;
}

int solution(string str1, string str2) {
    int answer = 0;
    int unionset = 0;
    int intersection = 0;
    vector<string> str1_set;
    vector<string> str2_set;
    
    str1_set = get_multipleSet(str1);
    str2_set = get_multipleSet(str2);
    
    if(str1_set.size() == 0 && str2_set.size() == 0){
        return 65536;
    }

    int *visit = new int[str2_set.size()];
    for(int i = 0; i < str2_set.size(); i++){
        visit[i] = 0;
    }

    // Get intersection set size
    for(int i = 0; i < str1_set.size(); i++){
        for(int j = 0; j < str2_set.size(); j++){
            if(visit[j] == 1){
                continue;
            }

            bool is_same = true;
            for(int k = 0; k < 2; k++){
                int diff = abs(int(str1_set[i][k]) - int(str2_set[j][k]));
                if(diff != 0 && diff != 32){
                    is_same = false;
                    break;
                }
            }

            if(is_same){
                visit[j] = 1;
                intersection++;
                break;
            }
        }
    }

    // Get union set size
    unionset += str1_set.size();
    for(int i = 0; i < str2_set.size(); i++){
        if(visit[i] == 0){
            unionset++;
        }
    }

    answer = int((float(intersection) / float(unionset)) * 65536);
    return answer;
}

int main(){
    cout << solution("handshake", "shake hands") << endl;
    cout << solution("FRANCE", "french") << endl;
    cout << solution("aa1+aa2", "AAAA12") << endl;
    cout << solution("E=M*C^2", "e=m*c^2") << endl;
    
    return 0;
}