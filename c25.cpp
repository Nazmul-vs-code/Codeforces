#include <iostream>
using namespace std;

int main()
{
    int n, h, result = 0;
    int height_friends[1000];
    cin >> n >> h;
    for (int i = 0; i < n; i++)
    {
        cin >> height_friends[i];

        if (height_friends[i] > h)
        {
            result = result + 2;
        }
        else if(height_friends[i]<=h )
        {
            result++;
        }
    }
    cout<<result;
    return 0;
}
