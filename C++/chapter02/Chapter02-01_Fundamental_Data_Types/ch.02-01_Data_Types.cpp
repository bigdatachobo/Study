#include <iostream>

int main()
{
    using namespace std;

    bool bValue = false;
    cout << (bValue ? 1 : 0 ) << endl;

    char chValue = 'A';
    cout << chValue << endl;

    float fValue = 3.141592f;
    double dValue = 3.141592;
    long double lValue = 3.141592;

    cout << fValue << endl;
    cout << dValue << endl;
    cout << lValue << endl;

    // auto - 자동으로 지정
    auto aValue = 3.141592;
    auto aValue2 = 3.141592f;
    cout << aValue << endl;
    cout << aValue2 << endl;

    // sizeof() - 변수 유형 자동 지정
    cout << sizeof(aValue) << endl;
    cout << sizeof(aValue2) << endl;

    cout << sizeof(bool) << endl;
    cout << sizeof(bValue) << endl;

    int a(123); // direct initialization
    int b{ 123 }; // uniform initialization
    int c{ 4 };
    auto d(3.14);

    // 같은 데이터 타입일 경우에만 ","로 연결 가능
    int k = 0, l(456), m{ 123 };

    // 변수 사용하기 직전에 선언하는 트렌트로 바뀜.

    return 0;
}