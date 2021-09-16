#include <iostream>

using namespace std;

int main(){

    int x = 5;
    double d = 123.0;
    // 변수의 주소를 포인터 변수에 저장
    int *ptr_x;
    double *ptr_d;

    cout << *ptr_x << endl;

    int n = 45;

    int *ptr = &n; // modern c++

    cout << *ptr << endl;

    

    // ptr = &d;

    // doSomething(ptr);

    


}