#include <iostream> 
#include <typeinfo>
#include <iomanip> // setprecision

int main()
{
    using namespace std;

    float a = 1.0f;
    double d = a; // numeric promotion

    cout << typeid(d).name()  << endl;

    // numeric conversion

    int i = 2;
    char c = i;

    cout << static_cast<int>(c) << endl; // 48 ( i=30000 )

    double dd = 0.123456789;
    float f= dd;

    cout << std::setprecision(12) << f << " " << dd << endl;
    
    float ff = 3.14;
    int ii = f;

    cout << std::setprecision(12) << ff << " " << ii << endl;

    cout << 5u - 10u << endl;

    int iii = int(4.0); // C++ 스타일 형변환
    int j = (int)4.0; // C 스타일 형변환
    int k = static_cast<int>(4.0); // 최신 유형




    return 0;
}