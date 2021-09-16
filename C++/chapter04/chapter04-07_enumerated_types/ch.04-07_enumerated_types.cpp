#include<iostream>
#include<typeinfo>
#include<string>

enum Color // 사용자 정의 데이터 타입
{
    COLOR_BLACK,
    COLOR_RED,
    COLOR_BLUE,
    COLOR_GREEN, // 마지막 콜론이 있어도되고, 없어도되고 상관없음.
    COLOR_SKYBLUE,
    BLUE,
};   

enum Feeling
{
    HAPPY,
    JOY,
    TIRED,
    // BLUE,
};

int main()
{
    using namespace std;

    Color paint = COLOR_BLACK;
    Color house(COLOR_BLUE);
    // Color apple{ COLOR_RED };
    Color my_color = COLOR_BLACK;

    cout << my_color << endl;

    int color_id = COLOR_RED;
    cout << color_id << endl;

    int in_number;
    cin >> in_number;

    // if ( in_number == 0 ) {my_color = COLOR_BLACK};

    string str_input;

    std::getline( cin, str_input );

    // if ( str_input == "COLOR_BLACK" );

}