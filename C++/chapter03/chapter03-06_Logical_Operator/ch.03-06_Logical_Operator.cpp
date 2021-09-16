#include <iostream>

int main()
{
    using namespace std;

    // logical AND
    bool x = true;
    bool y = false;

    cout << (x && y) << endl;

    bool hit = true;
    int health = 10;

    if (hit == true && health < 20)
    {
        cout << "--> die " << endl;
    }
    else
        health -= 20;

    // logical OR
    bool a = true;
    bool b = false;

    cout << ( a || b ) << endl;

    int c = 5;
    int d = 5;

    if ( !(c == d) )
    {
        cout << " c doe not equal d " << endl;
    }
    else
    {
        cout << " c equals d " << endl;
    }

    int v = 1;

    if ( v==0 || v == 1 || v == 2 )
    {
        cout << " v is 0 or 1 " << endl;
    }


    // short circuit evaluation
    int i = 2;
    int j = 2;

    if ( i == 1 && j++ == 2) // &&는 왼쪽 계산 후 false 가 뜨면 오른쪽을 계산을 안함.(계산 빠르게 하기 위해서.)
    {
        //do something
    }

    cout << j << endl;

    // De Morgan's Law 분배 법칙이 적용되지 않음.
    bool k = true;
    bool o = false;

    // !( x && y );
    // !x || !y;

    // !( x || y );
    // !x && !y;

    // XOR
    // false false = false
    // false true = true
    // true false = true
    // true true = false

    if ( k != o) // XOR
    {
        // do something
    }

    bool v1 = true;
    bool v2 = false;
    bool v3 = false;

    bool r1 = v1 || v2 && v3;
    bool r2 = ( v1 || v2 ) && v3;
    bool r3 = v1 || ( v2 && v3 );

    cout << r1 << endl;
    cout << r2 << endl;
    cout << r3 << endl;


    }