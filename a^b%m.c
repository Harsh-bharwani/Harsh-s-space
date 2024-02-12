#include<stdio.h>
int power(int a,int b,int m){
    if(b==0) return 1;
    if(b==1) return a%m;
    int even=1,odd=1;
    if(b%2==0) {
        even=power(a,b/2,m);
        return (even*even)%m;
    }
    else {
        odd=power(a,b/2,m);
        return (odd*odd*a)%m;
    }
}
int main(){
    int a,b,m;
    scanf("%d%d%d",&a,&b,&m);
    int res=power(a,b,m);
    printf("%d",res);
}