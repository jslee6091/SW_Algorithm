#include <iostream>
using namespace std;

int solution(int n)
{
    int ans = 0;

    while(n != 0){
        if(n % 2 == 1){
            n -= 1;
            ans++;
        }
        n /= 2;
    }
    return ans;
}

int main(){
    cout << solution(5) << endl;
    cout << solution(6) << endl;
    cout << solution(5000) << endl;
    return 0;
}