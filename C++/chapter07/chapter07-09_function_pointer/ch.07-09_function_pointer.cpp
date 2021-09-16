#include<iostream>
#include<array>

using namespace std;

int func(){

    return 5;
}

int goo(){
    
    return 10;
}

void printNumbers( const array<int, 10> &my_array, bool print_even){

    for ( auto element : my_array){
        if ( print_even && element % 2 == 0) { cout << element; }
        if ( !print_even && element % 2 == 1) { cout << element; }
    }
    cout << endl;

}

int main(){

    int(*fcnptr)() = func; // 함수 주소를 갖고온다.

    cout << fcnptr() << endl;

    fcnptr = goo;

    cout << fcnptr() << endl;

    // array
    std::array<int, 10> my_array{ 0,1,2,3,4,5,6,7,8,9};

    for ( auto element : my_array){
        if (element % 2 == 0) { cout << element; }
    }

    printNumbers(my_array, true);
    printNumbers(my_array, false);

}