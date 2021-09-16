#include <iostream>
using namespace std;

int main()
{
    int x(0); // x = 0

    // 0 0x16b80f408
    cout << x << " " << &x << endl;

    {
        x = 1;
        cout << x << " " << &x << endl;
        //1 0x16b80f408
    }

    {
        int x = 2;
        cout << x << " " << &x << endl;
        // 2 0x16b80f404
    }

    return 0;
} // x가 여기까지 존재함. 이후에는 적용 안됨.