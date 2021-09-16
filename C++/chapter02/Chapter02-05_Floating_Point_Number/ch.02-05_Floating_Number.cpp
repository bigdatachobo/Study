#include <iostream>
#include <iomanip>
#include <limits>
#include <cmath>

int main()
{
    using namespace std;

    float f;
    double d;
    long double ld;

    cout << sizeof(f) << endl;
    cout << sizeof(d) << endl;
    cout << sizeof(ld) << endl;

    cout << numeric_limits<float>::max() << endl; // 3.40282e+38
    cout << numeric_limits<double>::max() << endl; // 1.79769e+308
    cout << numeric_limits<long double>::max() << endl; // 1.79769e+308
    
    cout << numeric_limits<float>::lowest() << endl; // -3.40282e+38
    cout << numeric_limits<double>::lowest()  << endl; // -1.79769e+308
    cout << numeric_limits<long double>::lowest()  << endl; // -1.79769e+308
    
    float ff(3.14); // 3.14 = 31.4 * 0.1 = 314e-2
    double dd(3.141592);

    cout << 3.14 << endl;
    cout << 31.4e-1 << endl;
    cout << 31.4e-2 << endl;
    cout << 31.4e1 << endl;
    cout << 31.4e2 << endl;

    cout << std::setprecision(16) << endl; //  표시될 자릿수 설정
    cout << 1.0 / 3.0 << endl;

    float fff(123456789.0f); // 10 significant digits
    cout << std::setprecision(9) << endl; //  표시될 자릿수 설정
    cout << fff << endl; // 123456792

    double ddd(0.1);
    double d2( 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1);
    cout << ddd << endl;
    cout << std::setprecision(17) << endl; //  표시될 자릿수 설정
    cout << ddd << endl; // / 0.10000000000000001
    cout << d2 << endl; //0.99999999999999989 오차가 누적됨.

    // 이런 숫자가 나오면 안된다.
    double zero = 0.0;
    double posinf = 5.0 / zero;
    double neginf = -5.0 / zero;
    double nan = zero / zero;

    cout << posinf << endl; // inf
    cout << neginf << endl; // -inf
    cout << nan << endl; // nan

    // isnan
    cout << posinf << " " << std::isnan(posinf) << endl;
    cout << neginf << " " << std::isnan(neginf) << endl;
    cout << nan << " " << std::isnan(nan) << endl;

    // isinf
    cout << posinf << " " << std::isinf(posinf) << endl;
    cout << neginf << " " << std::isinf(neginf) << endl;
    cout << nan << " " << std::isinf(nan) << endl;
 
    return 0;
}