#include<stdio.h>
void print(int i,int n){
    if(i==n) {printf("%d",n); 
              return;}
    printf("%d",i++);
    print(i,n);

}
int main()
{
    int n;
    scanf("%d",&n);
   print(1,n);

}