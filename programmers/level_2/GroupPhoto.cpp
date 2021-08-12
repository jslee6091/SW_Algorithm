#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int answer;
bool visited[8];
string friends = "ACFJMNRT";

void permute(int count, char arr[], vector<string> data)
{
    // 전체 8개의 원소 모두 나열했을 경우
    if (count == 8)
    {
        for (int i = 0; i < data.size(); i++)
        {
            char N1 = data[i][0];
            char N2 = data[i][2];
            char cond = data[i][3];
            int dist = data[i][4] - '0';
            dist++;

            int Idx;
            int IIdx;
            Idx = IIdx = -1;

            // 조건에 해당하는 문자의 인덱스 구하기
            for (int j = 0; j < 8; j++)
            {
                if (arr[j] == N1) Idx = j;
                if (arr[j] == N2) IIdx = j;
                if (Idx != -1 && IIdx != -1) break;
            }

            // 두 문자의 위치가 조건을 만족하지 않으면 return
            if (cond == '=' && abs(Idx - IIdx) != dist) return;
            if (cond == '<' && abs(Idx - IIdx) >= dist) return;
            if (cond == '>' && abs(Idx - IIdx) <= dist) return;
        }

        // 조건을 만족하는 경우 1 더하고 종료
        answer++;
        return;
    }

    // 순열을 통해 요소들이 배치 되는 모든 경우를 체크
    for (int i = 0; i < 8; i++)
    {
        if (visited[i] == true) continue;
        visited[i] = true;
        arr[count] = friends[i];
        permute(count + 1, arr, data);
        visited[i] = false;
    }
}

int solution(int n, vector<string> data)
{
    // 문자의 순열을 저장할 문자 배열(NULL로 초기화하면 warning 발생)
    char arr[8] = {'0', };
    answer = 0;
    permute(0, arr, data);
    return answer;
}

int main(){
    // 조건을 만족하는 순열의 개수를 찾는 문제
    cout << solution(2, {"N~F=0", "R~T>2"}) << endl;
    cout << solution(2, {"M~C<2", "C~M>1"}) << endl;
}