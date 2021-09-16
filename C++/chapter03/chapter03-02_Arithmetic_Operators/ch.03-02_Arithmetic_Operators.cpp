#include <iostream>

int main()
{
    using namespace std;

    // +, -
    int x = 7;
    int y = 4;
    

    cout << x/y << endl;
    cout << float(x) / y << endl;
    cout << x / float(y) << endl;
    cout << float(x)/float(y) << endl;

    cout << -5 / 2  << endl;
    cout << 5 / 2 << endl;

    int z = x;
    z += y; // z = z + y;
    

    return 0;
}