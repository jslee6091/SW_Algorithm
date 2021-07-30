#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
    int answer = 0;
    string temp = "";
    for(int i = 0; i<s.size(); i++){
        if(s[i] >= '0' && s[i] <= '9'){
            temp += s[i];
        }
        else if(s[i] == 'z'){
            temp += '0';
            i += 3;
        }
        else if(s[i] == 'o'){
            temp += '1';
            i += 2;
        }
        else if(s[i] == 't'){
            if(s[i + 1] == 'w'){
                temp += '2';
                i += 2;
            }
            else if(s[i + 1] == 'h'){
                temp += '3';
                i += 4;
            }
        }
        else if(s[i] == 'f'){
            if(s[i + 1] == 'o'){
                temp += '4';
                i += 3;
            }
            else if(s[i + 1] == 'i'){
                temp += '5';
                i += 3;
            }
        }
        else if(s[i] == 's'){
            if(s[i + 1] == 'i'){
                temp += '6';
                i += 2;
            }
            else if(s[i + 1] == 'e'){
                temp += '7';
                i += 4;
            }
        }
        else if(s[i] == 'e'){
            temp += '8';
            i += 4;
        }
        else if(s[i] == 'n'){
            temp += '9';
            i += 3;
        }
    }
    answer = stoi(temp);
    return answer;
}

int main(){
    cout << solution("one4seveneight") << endl;
    cout << solution("23four5six7") << endl;
    cout << solution("2three45sixseven") << endl;
    cout << solution("123") << endl;
}