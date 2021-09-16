#include<iostream>

using namespace std;

int main(){

    int *ptr = nullptr;
    int **ptrptr = nullptr; //2차원 행렬 구할때 많이 씀

    int value = 5;

    ptr = &value;

    ptrptr = &ptr;

    cout << ptr << " " << *ptr << " "<< &ptr << endl;
    cout << ptrptr << " " << *ptrptr << " "<< &ptrptr << endl;
    cout << *(*ptrptr) << endl;

    int ***ppptr, ****pppptr;

    const int row = 3;
    const int col = 5;

    const int s2da[row][col]={
        {1,2,3,4,5},
        {6,7,8,9,10},
        {11,12,13,14,15}
    };

    int *matrix = new int[row*col];

    for (int r = 0; r < row; ++r)
        for(int c = 0; c < col; ++c)
            matrix[ c + col * r ]  = s2da[r][c];
    
    for(int r = 0; r < row; ++r){
        for(int c = 0; c < col; ++c){
            cout << matrix[ c + col * r]  << " ";
        }    
        cout << endl;
    }

    
    // // 이중 포인터 이용한 배열
    // int **matrix = new int*[row];

    // // 행별로 열 동적메모리 할당
    // for(int r = 0; r < row; ++r)
    //     matrix[r] = new int[col];

    // // matrix에 컬럼값 넣기
    // for (int r = 0; r < row; ++r)
    //     for (int c = 0; c < col; ++c)
    //         matrix[r][c] = s2da[r][c];

    // for(int r = 0; r < row; ++r){
    //     for(int c = 0; c < col; ++c)
    //         cout << matrix[r][c] << ' ';
    //     cout << endl;
    // }

    // // delete
    // for(int r = 0; r < row; ++r)
    //     delete[] matrix[r];

    // delete[] matrix;
    
 }