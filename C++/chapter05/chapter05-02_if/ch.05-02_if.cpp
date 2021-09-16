#include<iostream>

using namespace std;

int min( int x, int y )
{
    // if ( x > y )
    //     return y;
    // else 
    //     return x;

    return (x > y ) ? y : x; // 삼항 연산자.
}

int main()
{
    int x;
    cin >> x;

    if (x > 10)
        {
            cout << x << " is greater than 10 " << endl;
            cout << " Test 1 " << endl;
        }
    else
        {
            cout << x << " not greater than 10 " << endl;
            cout << " Test 1 " << endl;
        }

    if(1)
    {
        int x = 5;
    }
    else
    {
        int x = 6;
    }

    cout << x << endl; // cin

    if(x > 10)
    {
        cout << " x is greater than 10 " << endl;
    }
    else if (x < 10)
    {
        cout << " x is less than 10 " << endl;
    }
    else // if ( x == 10 )
    {
        cout << " x is exact 10 " << endl;
    }

    if( x >= 10 )
    {
        if( x >= 20)
            cout << " x is over 20 " << endl;
    }
    else
    {
        cout << " x is between 10 and 20 " << endl;
    } 

    int x1, y;
    cin >> x1 >> y;

    if ( x1 > 0 &&  y > 0 )
        cout << " both numbers are positive " << endl;    
    else if( x1 > 0 ||  y >  0)
        cout << " one of the numbers is positive " << endl;
    else    
        cout << " Neither number is positive " << endl;

    if ( x > 10 )
        cout << "A" << endl;
    else if ( x == -1 )
        return 0;
    else if (x < 0)
        cout << "B" << endl;
    
    if ( x > 10 ) //;
    {

    }

    if ( x = 0) // if ( x == 0 ), 의미 ->  x=0; if (x)
        cout << x << endl;

    cout << x << endl;             
    return 0;
}