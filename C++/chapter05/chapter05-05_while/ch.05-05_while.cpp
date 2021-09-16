#include<iostream>

using namespace std;

int main()
{   
    cout << " While - loop test " << endl;
    int count = 0;

    while (1)
    {
        cout << count << endl;
        ++count;

        if ( count == 10) break;
    }

    cout << " while - loop test minus " << endl;
    unsigned int counts = 10;

    while ( counts < 100 )
    {
        if (counts % 5 == 0 ) cout << "Hello " << counts
         << endl;
            // 몇번에 한 번씩 Hello 출력

        counts++;
    }

    int outer_count = 1;

    while ( outer_count <= 5 )
    {
         int inner_count = 1;
         while (inner_count <= outer_count)
         {
            cout << inner_count++ << " ";
         }

         cout << endl;
         ++outer_count;;;
         
    }

    // do-while문
    int selection;

    do
    {
        cout << "1. add" << endl;
        cout << "2. sub" << endl;
        cout << "3. mult" << endl;
        cout << "4. div" << endl;
        cin >> selection;
    }while (selection <= 0 || selection >= 5);
    
    cout << " You selected " << selection << endl;
    
    


    return 0;
}