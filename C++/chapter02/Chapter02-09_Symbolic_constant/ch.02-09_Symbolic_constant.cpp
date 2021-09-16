#include <iostream>
#include "Header_files/MY_CONSTANT.h"

void printNumber( int my_number )
{
    using namespace std;
    cout << my_number << endl;
}

int main()
{
    using namespace std;

    const double gravity{ 9.8 }; // 초기화를 반드시 해줘야 한다.
    // double const gravity{ 9.8 }

    printNumber(123);
    printNumber(gravity);

    double radius;
    cin >> radius;
    double circumference = 2.0 * radius * constants::pi;
    cout << circumference << endl;

    return 0;
}