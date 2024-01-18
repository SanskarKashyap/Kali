// #find username out of email 

#include <iostream>
using namespace std ;

int main ()
{

    string email ; 
    cout << "Enter your email : " ;
    cin >> email ;
    int i = email.find("@") ;   
    string username = email.substr(0,i) ;
    cout << "Your username is : " << username << endl ;
    

    return 0 ; 
}