#include <iostream>
using namespace std;

class Rectangle
{
private:
    int length;
    int breadth;

public:
    Rectangle(int l = 0, int b = 0)
    {
        length = l;
        breadth = b;
    }
    int area()
    {
        return length * breadth;
    }
    int perimeter()
    {
        return 2 * (length + breadth);
    }
    void changeLength(int l)
    {
        length = l;
    }
    void changeBreadth(int b)
    {
        breadth = b;
    }

    ~Rectangle()
    {
        cout << "Destructor" << endl;
    }
};

int main()
{
    Rectangle r, r2(10, 15),r3;
    r.changeLength(10);
    r.changeBreadth(5);
     cout << "Area of R is " << r.area() << endl;
    cout << "Perimeter of R is " << r.perimeter() << endl;
    cout << "Area of R2 is " << r2.area() << endl;
    cout << "Perimeter of R2 is " << r2.perimeter() << endl;

    Rectangle *p ;
    p = new Rectangle(4,8) ; // p is pointing to r in heap
    // Rectangle *p = new Rectangle(7, 5);
    cout << "Area of P is " << p->area() << endl;

    Rectangle * p2 ; 
    p2 = &r3 ; // p2 is pointing to r3 in stack
    p2->changeLength(11);
    p2->changeBreadth(6);
    cout << "Area of P2 is " << p2->area() << endl;

    delete p;


    return 0;
}
