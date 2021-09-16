#include<iostream>
#include<string>

using namespace std;

struct Employee // 2 + (2) + 4 + 8 = 14 + 2 // padding 
{
    short id; // 2 bytes -> 2바이트는 배치가 잘 안된다. 4로 배치됨.
    int age;  // 4 bytes
    double wage; // 8 bytes // 순서 배치도 short -> int -> double 순으로 해준다.
};

int main()
{
    Employee emp1;
    
    cout << sizeof(Employee) << endl;
    
    return 0;
}