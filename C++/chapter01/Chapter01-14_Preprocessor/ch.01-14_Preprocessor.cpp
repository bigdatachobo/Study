#include <iostream>
#include <algorithm> // max 포함한 헤더

using namespace std;

#define MAX(a,b) ((a > b) ? a : b) // 매크로 - 'MY_NUMBER'를 만나면 '9'로 교체해버림
// #define LIKE_APPLE
// define 효과는 파일 안에서만 적용이됨.

int main(void)
{
    cout << MAX(1, 2) << endl;
    cout << std::max(1+3, 2) << endl;

#ifdef LIKE_APPLE
    cout << "Apple" << endl;
#else
    cout << "Orange" << endl;
#endif    

    return 0;
}