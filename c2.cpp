#include <iostream>
using namespace std;

int main()
{
    int a, b, c, solved_problem = 0;
    int n, count;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >>a>>b>>c;
        count = a + b + c;
        if (count >= 2)
        {
            solved_problem++;
        }
    }
    cout<<solved_problem;

    return 0;
}