#include<iostream>

int main(){
    using namespace std;

    int value = 5;
    const int *ptr1 = &value; // 값 고정
    int *const ptr2 = &value; // 주소 고정
    const int *const ptr3 = &value; // 값, 주소 고정
    
    


    return 0;


}