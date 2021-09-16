#include <iostream>
#include <limits>

int main()
{
    using namespace std;

    char c1(65); // c1 = 65, c1
    char c2('A'); // "Hello, World" // std::string(문자열)

    cout << c1 << " " << c2 << " " << int(c1) << " " << int(c2) << endl;
    
    // 강제 변환 방법
    // C style casting
    cout << (char)65 << endl;
    cout << (int)'A' << endl;

    // C++ style casting
    cout << char(65) << endl;
    cout << int('A') << endl;

    // compiler에게 확인 후 변환 방법
    cout << static_cast<char>(65) << endl;
    cout << static_cast<char>('A') << endl;

    char ch(97);
    cout << ch << endl;
    cout << static_cast<int>(ch) << endl;
    cout << ch << endl;

    // char c3(65);

    // cin >> c3;
    // cout << c3 << " " << static_cast<int>(c3) << endl;

    // cin >> c3;
    // cout << c3 << " " << static_cast<int>(c3) << endl;

    // cin >> c3;
    // cout << c3 << " " << static_cast<int>(c3) << endl;

    char c4(65);

    cout << sizeof(char) << endl;
    cout << (int)std::numeric_limits<char>::max() << endl;
    cout << (int)std::numeric_limits<char>::lowest() << endl;

    cout << sizeof(unsigned char) << endl;
    cout << (int)std::numeric_limits<unsigned char>::max() << endl;
    cout << (int)std::numeric_limits<unsigned char>::lowest() << endl;

    cout << int('\n') << endl;
    cout << "This is first line \tsecond line\n";
    cout << "This is first line \" " << endl;
    cout << "second line \n";
    cout << "\a"; // 소리나는 코드

    wchar_t c;
    char32_t c5;
    

    return 0;
}