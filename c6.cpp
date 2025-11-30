#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
    int matrix[5][5];
    int rowind, colind, centerrow = 2, centercol = 2, moves;

    for (int i = 0; i < 5; i++)
    {
        for (int l = 0; l < 5; l++)
        {

            cin >> matrix[i][l];
            if (matrix[i][l] == 1)
            {
                rowind = i;
                colind = l;
            }
        }
    }

    moves = abs(rowind - centerrow) + abs(colind - centercol);
    cout << moves<<endl;

    return 0;
}