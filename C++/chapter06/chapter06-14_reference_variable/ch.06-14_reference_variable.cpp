#include<iostream>

using namespace std;

void doSomething(const int &n ){
    cout << &n << endl;
    // n = 10; 함수가 n 값을 바꾸지 못하게 한다.
    cout << "In do Something" << n << endl;
}

struct Something{

    int v1;
    float v2;
};

struct Other{

    Something st;
};

void doSomething2( const int& x){

    cout << x << endl;
}

int main(){

    int value = 5;

    int *ptr = nullptr; // 포인터값 초기화
    ptr = &value;

    int &ref = value; // 참조 value의 별명

    cout << ref << endl;

    ref = 10;

    cout << value << " " << ref << endl;

    cout << &value << endl;
    cout << &ref << endl;
    cout << ptr << endl;
    cout << &ptr << endl;

    // reference
    // int x = 5;
    // int &ref2 = x; //초기화를 꼭 해야한다.

    const int y = 8;
    const int &ref3 = y;

    int value1 = 5;
    int value2 = 10;
    
    int &ref4 = value1;

    cout << ref4 << endl;

    ref4 = value2;

    cout << ref4 << endl;

    //

    int n = 5;

    cout << n << endl;

    doSomething(n);

    cout << n << endl;

    Other ot;

    int &v1 = ot.st.v1; // 길어지면 레퍼런스 이용한다.
    v1 = 1.0;

    int value5 = 5;
    int *const ptr5 = &value;
    int &ref5 = value;

    *ptr = 10;
    ref = 10;

    // Reference와 const

    const int x = 5;
    const int &ref_x = x;

    // 

    const int &ref_y = 3 + 4;

    cout << ref_y << endl;
    cout << &ref_x << endl;

    doSomething2(1);
    doSomething2(3 + 8); // const 레퍼런스 이용시 파라마터 입력시 따로 변수를 할당하지 않아도 된다.
}