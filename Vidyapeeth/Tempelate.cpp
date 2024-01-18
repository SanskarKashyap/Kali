#include <iostream>
using namespace std;

// write a Max() function template for 2 numbers

template <class T> // spetial feature of C++ 
T Max(T a, T b)
{
    if (a > b)
    {
        return a;
    }
    return b ; 
}

int  main()
{
    cout << Max(10, 5) << endl;
    cout << Max(12.5f, 17.3f);
    return 0 ; 
}
