#include <iostream>
using namespace std;

int main()
{   
    int x = 2; // x is a variable, 2 is a literal.

    cout << x + 2 << endl;

    cout <<  - x << endl; // unary 단항 연산자

    cout <<  1 + 2 << endl; // binary  이상 연산자

    x = - 2;

    int y = ( x > 0 ) ? 1 : 2; // ternary 삼항연산자- 비교 분기 포함.

    cout <<  y << endl;

    cout << "My Home" << endl;

    return 0;
}