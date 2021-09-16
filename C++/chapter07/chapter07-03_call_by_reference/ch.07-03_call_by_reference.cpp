#include<iostream>
#include<cmath> // sin(), cos()

using namespace std;

void addOne(int &y){
    cout << y << " " << &y << endl;

    y  = y + 1;
}

void getSinCos( const double &degrees, double &sin_out, double &cos_out){

    static const double pi = 3.141592 / 180.0;

    const double radians = degrees * pi;
    
    sin_out = std::sin(radians);
    cos_out = std::cos(radians);
}

void foo( const int &x){ // 이 형태를 가장 많이 쓴다.
    cout << x << endl;
}

typedef int* pint;
void foo2( pint &ptr ){ // 이 형태를 가장 많이 쓴다.
    cout << ptr << " " << &ptr << endl;
}

// void printElement( int (&arr)[4] )
void printElement(vector<int>& arr){


}

int main(){

    int x = 5;
    cout << x << " " << &x << endl;

    addOne(x); // x라는 변수 자체가 넘어가버림.
    cout << x << " " << &x << endl;

    double sin(0.0);
    double cos(0.0);

    getSinCos( 30.0, sin, cos);

    cout << sin << " " << cos << endl;

    foo(6);

    // 포인터에 대한 레퍼런스 전달

    int i = 5;
    //int *ptr = &i;
    pint ptr = &i;


    cout << ptr << " " << &ptr << endl;
    foo2(ptr);

    // array를 참조변수로 전달하는 방법

    // int arr[]{1,2,3,4};
    vector<int> arr{1,2,3,4};

    return 0;

}