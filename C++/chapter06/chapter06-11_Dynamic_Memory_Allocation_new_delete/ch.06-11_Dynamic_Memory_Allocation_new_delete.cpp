#include<iostream>

using namespace std;

int main(){
    
    // var = 7;
    int *ptr = new (std::nothrow)int(7); // 메모리 os로부터 할당 받음.
    // (std::nothrow) 오류를 발생시키지 않고 메모리 할당 받음. 메모리가 꽉차 있을시
    cout << ptr << endl;
    cout << *ptr << endl;

    delete ptr; // 메모리 os에 반환.
    ptr = nullptr;// 의미없는 값이라 기록해두는것.

    cout << "After delete" << endl;
    if (ptr != nullptr){
        cout << ptr << endl;
        cout << *ptr << endl;
    }
    else{
        cout << " Could not allocate the memory " << endl;
    }

    int *ptr2 = ptr;

    delete ptr;
    ptr = nullptr;
    // ptr2 = nullptr;
    // *ptr2

    // 메모리 누수, memory leak
    while (true)
    {
        int *ptr = new int;
        cout << ptr << endl;
        delete ptr;
        ptr = nullptr;
    }
    


    return 0;
}