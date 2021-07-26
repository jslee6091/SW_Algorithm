#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int solution(vector<int> nums)
{
    auto answer = 0;
    // 뽑아야 하는 폰켓몬 개수
    answer = nums.size() / 2;
    
    // nums 요소들의 번호 종류 수를 구하기 위해 nums vector 중복 제거
    sort(nums.begin(), nums.end());
    nums.erase(unique(nums.begin(), nums.end()), nums.end());
    
    // 뽑아야 하는 폰켓몬 수가 nums의 전체 종류의 수보다 크면 정답을 변경
    if (answer > nums.size()){
        answer = nums.size();
    }
    
    return answer;
}

int main(){
    cout << solution({3,1,2,3}) << endl;
    cout << solution({3,3,3,2,2,4}) << endl;
    cout << solution({3,3,3,2,2,2}) << endl;
    return 0;
}

/* 다른 사람의 풀이 1
int solution(vector<int> nums)
{
    unordered_map<int, int> hash;

    for (auto num: nums) {
        hash[num] += 1;
    }

    return min(hash.size(), nums.size() / 2);

}
*/

/* 다른 사람의 풀이 2
int solution(vector<int> nums) {
    unordered_set<int> s(nums.begin(), nums.end());

    return min(nums.size() / 2, s.size());
}
*/