#include<iostream>
#include<cstring>

using namespace std;

int main(){
   
    char source[] = "Copy this!";
    char dest[50];
    strcpy(dest, source);
    
    cout << "Source : " << source << endl;
    cout << "Destination : " << dest << endl;

    //strcat() - 끝에 동일한 문자열 복사해서 덧붙임.
    //strcmp() - 두 문자열 동일한지 확인, 같으면 0을 리턴

    strcat(dest, source);

    cout << "Source : " << source << endl;
    cout << "Destination : " << dest << endl;

    // cout << strcmp( source, dest) << endl;

    if( strcmp(source, dest) == 0 ){
        cout << "strcmp 가 0을 리턴함." << endl;
    }
}