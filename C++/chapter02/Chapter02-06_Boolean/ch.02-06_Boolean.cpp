#include <iostream>

bool isEqual( int a, int b)
{
    bool result = (a == b);

    return result;
}

int main()
{
    using namespace std;

    bool b1 = true; // copy initialization
    bool b2(false); // direct ...
    bool b3{ true }; // uniform ...

    cout << std::boolalpha; // true / false로 출력되게 해줌.
    cout << b3 << endl;
    cout << b1 << endl;

    // "!" not operator
    cout << !true << endl;
    cout << !false << endl;

    // "&&" and operator
    cout << " " << endl;
    cout << "And OPERATOR" << endl;
    cout << (true && true) << endl; // true
    cout << (true && false) << endl; // false
    cout << (false && true) << endl; // false
    cout << (false && false) << endl; // false

    // "||" or operator
    cout << " " << endl;
    cout<< "OR OPERATOR" << endl;
    cout << (true || true) << endl; // true
    cout << (true || false) << endl; // true
    cout << (false || true) << endl; // true
    cout << (false || false) << endl; // false
    cout << " " << endl;

    // "if문"
    if(true)
    {
        cout << "This is true. " << endl;
        cout << "True second line " << endl;
    }
    else
    {
        cout << "This is false." << endl;
    }

    // "bool" 판별 함수
    cout << std::boolalpha;
    cout << isEqual(1,1) << endl;
    cout << isEqual(0,3) << endl;
    cout << " " << endl;

    if (1)
    {
        cout << "---> True" << endl;
        cout << " " << endl;
    }
    else
    {
        cout << "---> False" << endl;
        cout << " " << endl;
    }

    int num;

    cin >> num;

    if (num % 2 == 0)
    {
        cout << "---> 짝수 입니다." << endl;
    }
    else
    {
        cout << "---> 홀수 입니다." << endl;
    }

    // bool bb; // 0(false), 1(true)

    // cin >> bb;

    // cout << std::boolalpha;
    // cout << "---> Your input : " << bb << endl;

    return 0;

}