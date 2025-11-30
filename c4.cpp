#include <iostream>
using namespace std ;

int main(){
    int n , k , advanced = 0;
    cin>>n>>k;
    int score[n];
    for (int i = 0; i < n; i++)
    {
        cin>>score[i];
    }
    
    int cut = k-1;
    
    for (int l = 0; l < n; l++)
    {
        if (score[l] >= score[cut] && score[l]>0)
        {
            advanced++;
        }
        /* code */
    }
    

    printf("%d",advanced);
    return 0 ;
}