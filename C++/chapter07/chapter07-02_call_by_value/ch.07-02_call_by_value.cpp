#include<iostream>

using namespace std;

void doSomething(int y){

    cout << "In func " << y << " " << &y << endl;
}

int main(){

    doSomething(5);

    int x = 6;

    cout << "In main " << x << " " << &x << endl;

    doSomething(x); // 6이라는 값이 함수에 전달됨.
    doSomething(x + 1);

}