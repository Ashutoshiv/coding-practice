#include<iostream>
using namespace std;

class fact{
	int n,f, i,;
	public:
		void in(){
			cout<<"\n Enter any number: ";
			cin>>n;
		}
		
		void cal(){
			f=1;
			for(i=1; i<=n;i++){f = f*i;
			}
		}
		void show(){
			f=1;
			if(n<0){
				cout<<"No factorial for negative number!";
				
		}
			else if(n=0){
			
				cout<<"Factorial of 0 is 1";
				
		}
			else {
			
				f=1;
				for(i=1;i<=n;i++){
				f = f*1;
					
				}
			}
		}
	void show(){
		cout<<"\n Factorial is :"<<f;
	}	
};

int main(){
	fact p;
	p.in();
	p.call();
	p.show();
}
