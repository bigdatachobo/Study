#include <iostream>
#include <bitset>

int main()
{
    using namespace std;

    unsigned int a = 3;

    cout << std::bitset<4>(a) << endl;

    unsigned int b = a << 3;

    cout << std::bitset<8>(b) << " " << b << endl;

    cout << std::bitset<8>(a << 1) << " " << (a << 1) << endl;

    cout << std::bitset<8>(a << 2) << " " << (a << 2) << endl;
    cout << std::bitset<8>(a << 3) << " " << (a << 3) << endl;
    cout << std::bitset<8>(a << 4) << " " << (a << 4) << endl;

    unsigned c = 1024;

    cout << std::bitset<16>(c >> 1) << " " << (c >> 1) << endl;
    cout << std::bitset<16>(c >> 2) << " " << (c >> 2) << endl;
    cout << std::bitset<16>(c >> 3) << " " << (c >> 3) << endl;
    cout << std::bitset<16>(c >> 4) << " " << (c >> 4) << endl;

    unsigned d = 1024;

    cout << std::bitset<16>(d) << endl;
    cout << std::bitset<16>(~d) << " " << (~d)<< endl;

    unsigned int e = 0b1100;
    unsigned int f = 0b0110;

    cout << e << " " << f << endl;

    cout << std::bitset<4>( e & f ) << " " << (e & f) << endl; // AND
    cout << std::bitset<4>( e | f ) << " " << (e | f) << endl; // OR
    cout << std::bitset<4>( e ^ f ) << " " << (e ^ f) << endl; // XOR

    // Quiz
    // 1. 0110 >> 2 -> decimal?
    unsigned int u = 0b0110;
    cout << std::bitset<16>( u >> 2 ) << " " << ( u >> 2 ) << endl;
    // 5 | 12
    cout << std::bitset<8>(5) << " " << 5 << endl;
    cout << std::bitset<8>(12) << " " << 12 << endl;
    cout << std::bitset<8>(5 | 12) << " " << (5 | 12) << endl;
    // 5 & 12
    cout << std::bitset<8>(5 & 12) << " " << (5 & 12) << endl;
    // 5 ^ 12
    cout << std::bitset<8>(5 ^ 12) << " " << (5 ^ 12) << endl;


    return 0;


    
    
}