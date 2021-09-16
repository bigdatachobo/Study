#include <iostream>

int add( int a, int b )
{
    return a + b;
}

int main()
{
    using namespace std;

    int x = 1;
    // int v = add(x, ++x); // 이렇게 코딩하지 않는다. 결과값이 애매해짐.

    // cout << v << endl;

    return 0;
}