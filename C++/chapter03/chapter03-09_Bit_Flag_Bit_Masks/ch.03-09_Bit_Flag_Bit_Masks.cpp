#include<iostream>
#include<bitset>

int main()
{
    using namespace std;

    /* 
    bool item1_flag = false;
    bool item2_flag = false;
    bool item3_flag = false;
    bool item4_flag = false;
    ...
    */
    // ...

    // invokeEvent(item1_flag,item2_flag, item3_flag, ...)

    const unsigned char opt0 = 1 << 0;
    const unsigned char opt1 = 1 << 1;
    const unsigned char opt2 = 1 << 2;
    const unsigned char opt3 = 1 << 3;
    const unsigned char opt4 = 1 << 4;

    cout << bitset<8>(opt0) << "opt0" << endl;
    cout << bitset<8>(opt1) << "opt1" << endl;
    cout << bitset<8>(opt2) << "opt2" << endl;
    cout << bitset<8>(opt3) << "opt3" << endl;
    cout << bitset<8>(opt4) << "opt4" << endl;


    unsigned char items_flag = 0;

    cout << " No item " <<bitset<8>(items_flag ) << endl;

    // item0 on
    items_flag |= opt0;
    cout << " Item0 obtained" << bitset<8>(items_flag ) << endl;


    // item3 on
    items_flag |= opt3;
    cout << " Item3 obtained" << bitset<8>(items_flag ) << endl;

    // item3 lost
    items_flag &= ~opt3;
    cout << " Item3 lost" << bitset<8>(items_flag ) << endl;

    // has item1? // bitwise "&" 사용
    if ( items_flag & opt1 ) { cout << " Has item1 " << endl; }
    else { cout << " Not have item1 " << endl; }

    // has item0? // bitwise "&" 사용
    if ( items_flag & opt0 ) { cout << " Has item0 " << endl;}

    // obtain item 2,3

    items_flag |= (opt2 | opt3 );
    cout << bitset<8>( opt2 | opt3 ) << endl;
    cout << " Item 2 & 3 obtained" << bitset<8>(items_flag ) << endl;

    if ((items_flag & opt2) && !(items_flag & opt1))
    {
        items_flag ^= opt2; // items_flag에서 opt2를 없애버릴때 XOR연산자 "^"를 사용함.
        items_flag ^= opt1;
    }
    cout << bitset<8>( items_flag ) << endl;

    // bit mask
    const unsigned int red_mask = 0xFF0000;
    cout << bitset<32>(red_mask) << " " << "red mask" << endl;

    const unsigned int green_mask = 0x00FF00;
    cout << bitset<32>(green_mask) << " " << "green mask" << endl;

    const unsigned int blue_mask = 0x0000FF;
    cout << bitset<32>(blue_mask) << " " << "blue mask" << endl;

    unsigned int pixel_color = 0xDAA520; // 16진수 컬러
    cout << bitset<32>(pixel_color) << " "<< "pixel_color " << endl;

    unsigned char blue = pixel_color & blue_mask;
    cout << bitset<8>(blue) << " "<< "blue_color " << " " << int(blue) << endl;

    unsigned char green = (pixel_color & green_mask) >> 8;
    cout << bitset<8>(green) << " "<< "green_color " << " " << int(green) << endl;

    unsigned char red = (pixel_color & red_mask) >> 16;
    cout << bitset<8>(red) << " "<< "red_color " << " " << int(red) << endl;

}