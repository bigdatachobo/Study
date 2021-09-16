#include<iostream>

using namespace std;

inline int min(int x, int y){

    return x > y ? y : x;
}

int main(){

    cout << min(5,6) << endl;
    cout << min(3,2) << endl;

    // inline  적용시 이렇게 적용됨.
    cout << (5 > 6 ? 6:5) << endl;
    cout << (3 > 2 ? 2 : 3) << endl;

    
}