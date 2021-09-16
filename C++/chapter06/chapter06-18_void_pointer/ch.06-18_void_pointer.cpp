#include<iostream>

using namespace std;

// void pointer, generic pointer

int main(){

    int i = 5;
    float f = 3.0;
    char c = 'a';

    void *ptr = nullptr;

    ptr = &i;
    ptr = &f;
    ptr = &c;

    // cout << ptr + 1 << endl; // point 연산이 안됨.

    cout << &c << ' ' << ptr << endl;
    cout << &f << ' ' << ptr << endl;
    
}