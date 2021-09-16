#include<iostream>
#include<cmath>

using namespace std;

typedef int* pint;

void foo(const int *ptr){

    cout << *ptr << " " << ptr << " " << &ptr << endl;

}

void getSinCos( const double &degrees, double *sin_out, double *cos_out){

    static const double pi = 3.141592 / 180.0;

    const double radians = degrees * pi;
    
    *sin_out = 1.0;
    *cos_out = 2.0;
}

void foo2( const int *ptr, int *arr, int length){
    for (int i = 0; i < length; i++)
    {
        cout << arr[i] << endl;
    }
    arr[0] = 1.0;

    int x = 1;

    ptr = &x;
}

int main(){

    int value = 5;

    cout << value << " " << &value << endl;

    int *ptr = &value;

    cout << &ptr << endl;

    foo(ptr);

    double degrees = 30;
    double sin, cos;

    getSinCos(degrees, &sin, &cos);

    cout << sin << " " << cos << endl;
    cout << &sin << " " << &cos << endl;
    
    return 0;
}