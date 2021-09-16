#include<iostream>

namespace a { int my_var(10); }
namespace b { int my_var(20); }

int main()
{
    using namespace std;
    // using std::cout;
    // using std::endl;

    {
    using namespace a;
    cout << my_var << endl;
    }
    
    {
    using namespace b;
    cout << my_var << endl;
    }

    cout << "Hello " << endl;



}