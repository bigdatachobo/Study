#include <iostream>

int main()
{
    using namespace std;

    // 8진수
    // Octal :  0 1 2 3 4 5 6 7 10
    // Hexa  : 0 1 2 3 4 5 6 7 8 9 A B C D E F 10

    // 0011 1010 1111 (2진수)
    // 3A7F (16진수) - 짧아서 보기 편하다.

    int x = 012; // 앞에 '0'을 붙이면 8진수가 된다.
    cout << x << endl;

    int h = 0xF; // 앞에 '0x'을 붙이면 16진수가 된다.
    cout << h << endl;

    int b = 0b1010; // 앞에 '0b'를 붙이면 2진수가 된다.
    cout << b << endl;

    int b2 = 0b1011'1111'1010; // " ' " 중간에 삽입시 사람이 읽기 편하라고 삽입함, 컴파일러는 무시함.
    cout << b2 << endl; // 3066

    
    
}