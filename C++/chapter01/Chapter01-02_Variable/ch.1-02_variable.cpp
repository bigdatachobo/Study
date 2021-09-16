#include <iostream>
int main()
{
    // int x;

    // int y = 128; // initialization

    // int z(123); // initialization 위와 같은 의미



    // x = 123; // assignment 대입.
    // // "=": x라는 변수에 123을 저장
    // std::cout << x << std::endl;
    // // "&" 메모리 주소 표시
    // // 0x16cf97418
    // std::cout << &x << std::endl;

    // x = x + 2;
    // std::cout << x << std::endl;

    // x += 2;
    // std::cout << x << std::endl;

    // 연습 문제

    int x = 1;
    x = x + 2;
    std::cout << x << std::endl;

    int y = x;
    std::cout << y << std::endl;

    std::cout << x + y << std::endl;

    std::cout << x << std::endl;

    int z;
    std::cout << z << std::endl;

    return 0;
}