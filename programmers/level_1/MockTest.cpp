#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> person1;
    vector<int> person2;
    vector<int> person3;
    vector<int> score = {0,0,0};
    
    // person1의 찍는 방식 : 1,2,3,4,5,1,2,3,4,5, ...
    // person2의 찍는 방식 : 2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5, ...
    // person3의 찍는 방식 : 3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5, ...
    for (int i = 0; i<answers.size(); i++){
        // person1의 정답 삽입
        person1.push_back(i % 5 + 1);
        
        // person2의 정답 삽입
        if (i % 2 == 0){
            person2.push_back(2);
        }
        else{
            int temp = (i / 2) % 4;
            if (temp == 0){ person2.push_back(1);}
            else if (temp == 1){ person2.push_back(3);}
            else if (temp == 2){ person2.push_back(4);}
            else{ person2.push_back(5);}
        }
        
        // person3의 정답 삽입
        int temp2 = (i / 2) % 5;
        if (temp2 == 0){ person3.push_back(3);}
        else if (temp2 == 1){ person3.push_back(1);}
        else if (temp2 == 2){ person3.push_back(2);}
        else if (temp2 == 3){ person3.push_back(4);}
        else{ person3.push_back(5);}
    }
    
    // answers와 각 person들의 정답이 몇개가 일치하는지 확인
    for(int j = 0; j<answers.size(); j++){
        if (person1[j] == answers[j]){
            score[0]++;
        }
        
        if (person2[j] == answers[j]){
            score[1]++;
        }
        
        if (person3[j] == answers[j]){
            score[2]++;
        }
    }

    // 각 person 별 맞춘 정답 개수 중 최대값을 구하기
    int max_value = *max_element(score.begin(), score.end());

    // 가장 많은 정답을 맞춘 사람 찾아내기
    for (int k = 0; k < 3; k++){
        if (score[k] == max_value){
            answer.push_back(k + 1);
        }
    }
    return answer;
}

int main(){
    vector<int> input1 = {1,2,3,4,5};
    vector<int> input2 = {1,3,2,4,2};
    
    vector<int> result1 = solution(input1);
    vector<int> result2 = solution(input2);

    cout << "result 1 : ";
    for(int i = 0; i<result1.size(); i++){
        cout << result1[i] << " ";
    }
    cout << endl;

    cout << "result 2 : ";
    for(int i = 0; i<result2.size(); i++){
        cout << result2[i] << " ";
    }
    cout << endl;

    return 0;
}