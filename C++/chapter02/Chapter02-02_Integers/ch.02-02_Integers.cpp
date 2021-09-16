#include <iostream>
#include <cmath>
#include <limits>
#include <cstdint>

int main()
{
    using namespace std;

    short s = 1; // 2 bytes = 2 * 8bits = 16bits
    int   i = 1;
    long  l = 1;
    long long ll = 1;

    cout << std::pow(2, sizeof(short) * 8 -1 ) - 1 << endl; // 32767
    cout << std::numeric_limits<short>::max() << endl; // 32767
    cout << std::numeric_limits<short>::min() << endl; // -32768
    cout << std::numeric_limits<short>::lowest() << endl; // -32768
    cout << sizeof(long) << endl;
    cout << sizeof(long long) << endl;

    // s = 32767;
    // s = s + 1; // 32768

    // // -32768
    // cout << s << endl; // overflow

    s = -32768;
    s = s - 1; // -32769

    // -32769
    cout << s << endl; // overflow

    unsigned int j = -1;

    // 4294967295
    cout << j << endl;

    int k = 22 / 4;
    cout << k << endl; // 5
    cout << (float)22 / 4 << endl; // 5.5
    cout << 22 / (float)4 << endl; // 5.5

    std::int16_t u(5);
    std::int8_t myint = 65; // char 타입으로 변환됨.

    cout << myint << endl;

    std::int_fast8_t fi(5);
    std::int_least64_t fl(5);

    cout << fi << endl;
    cout << fl << endl;

    // void
    void *my_void;
    
    my_void = (void*)&fi;
    my_void = (void*)&fl; // 포인터 다룰때 많이 사용하게 됨.

    return 0; 
}