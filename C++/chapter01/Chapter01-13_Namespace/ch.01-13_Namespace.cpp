#include <iostream>

using namespace std;

namespace Myspace1
{

    int do_something( int a, int b )
    {
        return a + b;
    }
}

namespace Myspace2
{
    int do_something( int a, int b )
    {
        return a * b;
    }
}
int main()
{

    cout << Myspace1::do_something( 3, 4) << endl;
    cout << Myspace2::do_something( 3, 4) << endl;

    using namespace Myspace1;
    cout << do_something(5,6) << endl;

    // using namespace Myspace2;
    // cout << do_something(5,6) << endl;

    return 0;
}