#include<iostream>

using namespace std;

struct Rectangle
{
    int length;
    int width;
};

enum StudentName
{
    JACKJACK, // 0
    DASH,     // 1  
    VIOLET,   // 2
    NUM_STUDENTS, // 3
};

#define NUM_STUDENTS 100000; // 권장하지 않음, 동적할당을 권장함.

void doSomething(int students_scores[20])
{   
    cout << &students_scores << endl;
    cout << students_scores[0] << endl;
    cout << students_scores[1] << endl;
    cout << students_scores[2] << endl;
    cout << students_scores[3] << endl;
    cout << students_scores[4] << endl;
    cout << "size of doSomething" << endl;
    cout << sizeof(students_scores) << endl;
}

int main()
{
    int one_student_score; // 1 variable
    int student_scores[5]; // 5 int

    cout << sizeof(one_student_score) << endl;
    cout << sizeof(student_scores) << endl;

    one_student_score = 100;

    student_scores[0] = 100; // 1st element
    student_scores[1] = 80;  // 2nd element
    student_scores[2] = 90;  // 3rd element
    student_scores[3] = 50;  // 4th element
    student_scores[4] = 0;   // 5th element
    // student_scores[5] = 30;  // 6th element

    
    cout << student_scores[0] << endl; 
    cout << student_scores[1] << endl;
    cout << student_scores[2] << endl;
    cout << student_scores[3] << endl;
    cout << student_scores[4] << endl;
    // cout << student_scores[5] << endl;

    cout << (student_scores[0] + student_scores[1]) / 2.0 << endl;

    cout << " 구조체 " << endl;

    cout << sizeof(Rectangle) << endl;
    Rectangle rect_arr[10];

    cout << sizeof(rect_arr) << endl;

    rect_arr[0].length = 1;
    rect_arr[0].width = 2;

    cout << " array 초기화 " << endl;
    int my_array[5] = { 1, 2, 3, 4, 5 };
    
    cout << my_array[0] << endl;
    cout << my_array[1] << endl;
    cout << my_array[2] << endl;
    cout << my_array[3] << endl;
    cout << my_array[4] << endl;

    cout << " enum을 활용한 인덱싱 " << endl;

    cout << my_array[JACKJACK] << endl;
    cout << my_array[DASH] << endl;
    cout << my_array[VIOLET] << endl;
    cout << my_array[3] << endl;
    cout << my_array[4] << endl;

    cout << " cin " << endl;
    const int num_students = 5;
    // cin >> num_students; // 정수가 입력받아봐야 알 수 있는것. 결정되기 전의 값

    int students_scores[num_students] = {1,2,3,4,5,}; // 컴파일에선 확정된 값이 [] 안으로 들어가야 한다.

    cout << " 주소 찍어가며 확인 " << endl;

    cout << students_scores << endl;
    cout << &students_scores[0] << endl;
    cout << &students_scores[1] << endl;
    cout << &students_scores[2] << endl;
    cout << "size of main" << endl;
    cout << sizeof(students_scores) << endl;

    cout << " doSomething 주소 " << endl;

    doSomething(students_scores);

    return 0;
}