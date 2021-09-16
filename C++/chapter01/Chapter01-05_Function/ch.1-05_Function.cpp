#include <iostream>
using namespace std;

int multiply_two_numbers( int num_a, int num_b )
{
    int sum = num_a * num_b;

    return sum;
}

int add_two_numbers( int a, int b)
{
    return a+b;
}

void print_hello_world()
{
    cout << "Hello World" << endl;

    return;

    cout << "Hello World2" << endl;

}


int main(void)
{
    cout << multiply_two_numbers(1, 2) << endl;
    cout << multiply_two_numbers(3, 4) << endl;
    cout << multiply_two_numbers(8, 13) << endl;

    print_hello_world();

    int sum = add_two_numbers(3, 8);
    cout << sum << endl;

    return 0;
}