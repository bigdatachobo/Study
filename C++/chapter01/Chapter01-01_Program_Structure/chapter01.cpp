#include <iostream> // preprocessor directive
int main()
{   int x = 2; //리터럴, literal
    x = 5;
    int y = x + 3;
    /*
    주석 다는 방법 2가지
    1. "//"" 한줄씩
    2. 영역으로 주석처리하는 방법
    */

   int sight = 10;

   // ... 어떤 이유 마법의 물약을 먹어서 시야 거리가 0 이 된다.

   sight = 0;
   // 1+1 event
   // int cost = (num_items / 2) * price_per_item;
   

    std::cout << y << std::endl;

    return 0;

}
