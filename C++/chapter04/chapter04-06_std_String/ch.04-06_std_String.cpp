#include<iostream>
#include<string>
#include<limits>

int main()
{
    using namespace std;

    const char my_strs [] = "Hello, World";
    const string my_hello = "Hello, World";

    string my_ID = "123";

    cout << my_hello << endl;
    cout << my_ID << endl;

    cout << "Your name? ";
    string name;
    std::getline( cin, name );
    //cin >> name;

    cout << "Your age? ";
    string age;
    std::getline( std::cin, age );
    cout << name << " " << age << endl;

    // std::cin.ignore(32767, '\n'); //입력받는 글자 크기를 정해줌.
    // std::cin.ignore(std::numberic_limits<std::streamsize>::max(),'\n')

    string a("Hello, World");

    cout << a.length() << endl;


    return 0;
}