#include <iostream>

using namespace std;

// forward declaration 전방 선언
int add( int a, int b );
int multiply( int a, int b);
int subtract( int a, int b );

int main(void)
{
    cout << add(3,4) << endl;

    cout << subtract(3,4) << endl;

    cout << multiply(3,4) << endl;

    return 0;
}

// definition 정의
int add( int a, int b )
{
    return a + b;
}

int multiply( int a, int b)
{
    return a * b;
}

int subtract( int a, int b )
{
    return a - b;
}