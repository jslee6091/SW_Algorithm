#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

vector<string> solution(vector<string> record) {
    vector<string> answer;
    // 채팅방 이용 기록 저장
    vector<pair<string,string>> log;
    // 채팅방 이용했던 회원의 회원 정보 저장
    map<string, string> info;
    
    // 문자열 나누어서 유저 아이디, 닉네임, 채팅방 방문 기록을 저장
    for(int i=0; i<record.size(); i++){
        // Enter, Change, Leave 에 대한 정보
        string state = "";
        // 유저아이디
        string id = "";
        // 닉네임
        string nick = "";
        // 문자열을 각 단어로 나누기 위한 변수
        int flag = 0;
        
        // 문자열을 공백을 기준으로 한 단어씩 나누기(python의 split)
        for(int j=0; j<record[i].size(); j++){
            // 문자가 공백일 때 flag 1 증가 후 다음 반복문 실행
            if(record[i][j] == ' '){
                flag++;
                continue;
            }
            
            // flag 가 0이면 state에 해당함
            if(flag == 0){
                state += record[i][j];
            }
            // flag 가 1이면 유저 아이디에 해당함
            else if(flag == 1){
                id += record[i][j];
            }
            // flag 가 2이면 닉네임에 해당함
            else if(flag == 2){
                nick += record[i][j];
            }
        }
        
        // 회원의 이용 기록 저장 - state와 유저 아이디
        log.push_back(make_pair(state, id));
        
        // Leave인 경우 회원 정보에 아무 영향이 없으므로 pass
        if(state == "Leave"){
            continue;
        }
        // Enter, Change인 경우 회원 정보가 추가되거나 변경됨
        // 유저아이디가 없는 경우 닉네임과 함께 새로 삽입
        if(info.find(id) == info.end()){
            info.insert(make_pair(id,nick));
        }
        // 이미 있는 경우 닉네임 갱신(바뀌지 않았으면 상관없지만 바뀌었을 경우 반영하기 위함)
        else{
            info[id] = nick;
        }
    }
    
    // 채팅방 전체 이용 기록을 다시 조회하여 현재 회원 정보에 맞는 새 기록을 answer에 저장
    for(int i=0; i<log.size(); i++){
        string str = "";
        // 유저 아이디 문자열에 추가
        str += info[log[i].second];
        
        // state에 따라 다른 문장 삽입
        if(log[i].first == "Enter"){
            str += "님이 들어왔습니다.";
        }
        else if(log[i].first == "Leave"){
            str += "님이 나갔습니다.";
        }
        else if(log[i].first == "Change"){
            continue;
        }
        
        answer.push_back(str);
    }
    return answer;
}

int main(){
    vector<string> result = solution({"Enter uid1234 Muzi","Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"});
    
    for(string ss : result){
        cout << ss << endl;
    }
}