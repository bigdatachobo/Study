#include<iostream>

using namespace std;

void printArray( const int array[], const int length)
{
    for (int i = 0; i < length; i++)
    {
        cout << array[i] << " ";
    }
    cout << "" << endl;
    
};

int main()
{
    const int length = 5;
    int array[length] = { 3, 5, 2, 1, 4 };

    printArray(array, length);

    // swap
    // int temp = array[0];
    // array[0] = array[1];
    // array[1] = temp;

    int compare;
    int temp;
    for (int i = 0; i < length - 1; ++i)
    {
        for (int j = i + 1;  j < length; ++j)
        {
            if (array[i] > array[j])
            {
                temp = array[i];
                array[i]= array[j];
                array[j] = temp;
            }
        }
        
    }
    printArray(array,length);

    // Bubble sort
    
}