#include<iostream>
#include<vector>
#include<cstdint>

int main()
{   
    typedef float distance_t; // type 바꿀때도 여기만 바꾸면되서 유지 관리에 편함.

    double my_distance;
    distance_t home2work;
    distance_t home2school;

    using namespace std;
    std::int8_t i(97); // typedef으로 새롭게 정의한것.

    // vector<pair<string, int> > pairlist1;
    // vector<pair<string, int> > pairlist2;

    typedef vector<pair<string, int> > pairlist_t;
    using pairlist_t = vector<pair<string, int> >;

    pairlist_t pairlist1;
    pairlist_t pairlist2;


    return 0;
}