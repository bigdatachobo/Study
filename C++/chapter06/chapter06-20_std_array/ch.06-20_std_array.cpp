#include<iostream>
#include<array>
#include<algorithm>

using namespace std;

void printLength(const array<int,5>& my_arr){

    cout << my_arr.size() << endl;
}

int main(){

    //int array[5] = {1,2,3,4,5}

    std::array<int, 5> my_arr = {1,2,3,4,5};
    my_arr = {0,1,2,3,4};
    my_arr = {0,1,2};

    printLength(my_arr);

    array<int,5> my_arr2 = {1, 21, 3, 40, 5};

    for ( auto &element : my_arr2 ) // "&" 참조 사용하여 중간에 복사되는 과정을 줄일 수 있다.
        cout << element << " ";
    cout << endl;

    // 순방향 정렬
    std::sort( my_arr2.begin(), my_arr2.end());

    for ( auto &element : my_arr2 ) // "&" 참조 사용하여 중간에 복사되는 과정을 줄일 수 있다.
        cout << element << " ";
    cout << endl;

    // 역순 정렬
    std::sort( my_arr2.rbegin(), my_arr2.rend());

    for ( auto &element : my_arr2 ) // "&" 참조 사용하여 중간에 복사되는 과정을 줄일 수 있다.
        cout << element << " ";
    cout << endl;


}