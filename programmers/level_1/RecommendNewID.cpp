#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

// programmers 다른 사람들의 풀이 참고
string solution1(string new_id) {
    for (char& ch : new_id) if ('A' <= ch && ch <= 'Z') ch |= 32;

    string ret;
    for (char& ch: new_id) {
        if ('a' <= ch && ch <= 'z' ||
            '0' <= ch && ch <= '9' ||
            strchr("-_.", ch)) ret += ch;
    }

    new_id = ret;
    ret.clear();
    for (char& ch: new_id) {
        if (!ret.empty() && ret.back() == '.' && ch == '.') continue;
        ret += ch;
    }

    if (ret.front() == '.') ret.erase(ret.begin());
    if (ret.back() == '.') ret.pop_back();

    if (ret.empty()) ret = "a";
    if (ret.size() >= 16) ret = ret.substr(0, 15);
    if (ret.back() == '.') ret.pop_back();
    while (ret.size() <= 2) ret += ret.back();

    return ret;
}

// 다른 사람들의 풀이 2
string solution2(string new_id) {

    // 1 단계
    for(int i = 0; i < new_id.length(); i++)
        if (new_id[i] >= 'A' && new_id[i] <= 'Z') 
            new_id[i] = tolower(new_id[i]);

    // 2 단계 
    for(int i = 0; i < new_id.length(); ) {
        if ((new_id[i] >= 'a' && new_id[i] <= 'z') || (new_id[i] >= '0' && new_id[i] <= '9')
              || new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.')
        {
            i++;
            continue;
        }

        new_id.erase(new_id.begin() + i);
    }

    // 3 단계
    for(int i = 1; i < new_id.length(); ){
        if (new_id[i] == '.' && new_id[i - 1] == '.'){
            new_id.erase(new_id.begin() + i);
            continue;
        }
        else i++;
    }

    // 4 단계
    if (new_id.front() == '.') new_id.erase(new_id.begin());
    if (new_id.back() == '.') new_id.erase(new_id.end() - 1);

    // 5 단계
    if (new_id.length() == 0) 
        new_id = "a";

    // 6 단계
    if (new_id.length() >= 16){
        while(new_id.length() != 15){
            new_id.erase(new_id.begin() + 15);
        }
    }
    if (new_id.back() == '.') new_id.erase(new_id.end() - 1);

    // 7 단계
    if (new_id.length() <= 2){
        while(new_id.length() != 3){
            new_id += new_id.back();
        }
    }

    return new_id;
}

int main(){
    string result1 = solution1("...!@BaT#*..y.abcdefghijklm");
    string result2 = solution2("z-+.^.");
    
    cout << "result1 : " << result1 << endl;
    cout << "result2 : " << result2 << endl;
}