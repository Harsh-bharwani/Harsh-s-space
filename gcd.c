#include<stdio.h>
int gcd(int a,int b){int gcd=1;
int i=0;
    if(a%i==0 && b%i==0)
    gcd=i;
    i++;
    if(i==a+1 || i==b+1)
     return;
     
}
int main(){
    int a,b;
    scanf("%d%d",&a,&b);
    int res=gcd(a,b);
    printf("%d",res);
}
