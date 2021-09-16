#include <iostream> // cout, cin, endl, ...
#include <cstdio> // printf

int main(void)
{
    using namespace std; // 이 이후에 "std::"를 안 써도 된다.

    int x = 1024;
    double pi = 3.141592;

    cout << "I love this lecutre!\n"; // << std::endl;
    cout << "x is " << x << "\npi is " << pi << std::endl;
    cout << "abc" << "\t" << "def" << endl;
    cout << "ab" << "\t" << "cdef" << endl;
    cout << "\a"; // 사운드 생성 명령어

    // std:: 생략 가능
    int z=1;
    cout << "Before your input, z was " << z << endl;

    cin >> z; // 파이썬 input() 함수 같이 터미널 창에서 직접 입력하는 함수

    cout << "Your input is " << z << endl;

    return 0;
}