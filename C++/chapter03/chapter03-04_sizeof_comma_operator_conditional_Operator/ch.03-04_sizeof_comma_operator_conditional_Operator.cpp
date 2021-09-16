#include <iostream>

int main()
{
    using namespace std;

    // float a;
    // // sizeof -> 연산자임.
    // cout << sizeof(float) << endl; // 4바이트 = 32비트
    // cout << sizeof(a) << endl;; // 4바이트 = 32비트

    // comma operator 쉼표 연산자
    // int x = 3;
    // int y = 10;
    // //int z = (++y, ++x); 콤마 오퍼레이터를 풀어서 쓰면 밑에처럼 된다.
    // ++x;
    // ++y;
    // int z = y;

    // cout << x << " " << y << " " << z << endl;

    int a = 1, b = 10;
    int z;

    z = (++a, a + b);
    cout << z << endl;

    // 조건부 연산자 (conditional operator) - (Arithmetric if) - 삼항 연산자
    // 형태 - ( ) ? a : b

    bool onSale = true;
    const int price = (onSale == true) ? 10 : 100;

    cout << price << endl;

    int x = 5;

    cout << ( (x % 2 == 0) ? "even" : "odd") << endl;

    return 0;
}