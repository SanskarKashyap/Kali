//matrix multiplication

#include<iostream>
using namespace std ; 




int main()
{
    cout << "Enter the number of rows and columns of matrix A : " ;
    int m , n ;
    cin >> m >> n ;

    cout << "Enter the number of rows and columns of matrix B : " ;
    int p , q ;
    cin >> p >> q ;

    if (n != p)
    {
        cout << "Matrix multiplication not possible" ;
        return 0 ;
    }

    int A[m][n], B[p][q], C[m][q];

    cout << "Enter the elements of matrix A : " ;
    for (auto &x:A)
    {
        for(auto &y:x)
        {
            cin >> y ;
        }
    }

    cout << "Enter the elements of matrix B : " ;
    for (auto &x:B)
    {
        for(auto &y:x)
        {
            cin >> y ;
        }
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < q; j++)
        {
            C[i][j] = 0 ;
            for (int k = 0; k < n; k++)
            {
                C[i][j] += A[i][k] * B[k][j] ;
            }
        }
    }

    cout << "The resultant matrix is : " << endl ;

    for (auto &x:C)
    {
        for(auto y:x)
        {
            cout << y << " " ;
        }
        cout << endl ;
    }

    


    return 0 ; 
}