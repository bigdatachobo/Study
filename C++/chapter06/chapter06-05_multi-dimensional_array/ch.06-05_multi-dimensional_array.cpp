#include<iostream>

using namespace std;

int main()
{
    const int num_rows = 3;
    const int num_colums = 5;

    int array[num_rows][num_colums]=
    {
        {1,2,3,4,5},
        {6,7,8,9,10},
        {11,12,13,14,15}
    };

    for (int  row = 0; row < num_rows; ++row){
        for (int col = 0; col < num_colums; ++col){
            cout << array[row][col] << '\t';
        }
    }

    int array[5][4][3];
    
}