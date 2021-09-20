#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer(n * (n + 1) / 2, 0);
    
    int count = 0;
    int subcount = 0;
    int number = 1;
    int index = 0;
    int diff = 0;
    
    while(count < n){
        answer[index] = number;
        subcount++;
        number++;
            
        // 왼쪽 아래로 내려가기
        if(count % 3 == 0){
            diff++;
            if(subcount == n - count){
                subcount = 0;
                count++;
                index++;
                continue;
            }
            index += diff;
            
        }
        // 오른쪽 옆으로 이동
        else if(count % 3 == 1){
            if(subcount == n - count){
                subcount = 0;
                index -= diff;
                diff--;
                count++;
                continue;
            }
            index++;
        }
        // 왼쪽 위로 올라가기
        else{
            if(subcount == n - count){
                count++;
                index += diff;
                subcount = 0;
                continue;
            }
            index -= diff;
            diff--;
        }
        
        if(count == answer.size()){
            break;
        }
    }
    return answer;
}

int main(){
    vector<int> result1 = solution(4);
    vector<int> result2 = solution(5);
    vector<int> result3 = solution(6);

    for(int num : result1){
        cout << num << " ";
    }
    cout << endl;
    
    for(int num : result2){
        cout << num << " ";
    }
    cout << endl;
    
    for(int num : result3){
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}