#include<iostream>
#include<string>

using namespace std;

typedef int my_int;

void print( int x) {}

void print( const char *value){}
// void print( int value ){}

void print( unsigned int value) {}
void print(float value) {}

int add(int x, int y){

    return x + y;
}

double add(double x, double y){
    
    return x + y;
}

void getRandomValue( int &x) {}

void getRandomValue( double &x ) {}


int main(){

    cout << add(1,2) << endl;
    cout << add(3.0, 4.0) << endl;

    int x;
    getRandomValue(x);

    print(0u); // unsigned
    print("a");
    print(3.141592f); // float

}