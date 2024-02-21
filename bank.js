function Withdrawl(balance,wd_amt,type){
    let rem_balance=balance
    let upi_limit=20;
let atm_limit=10;
let tap_to_pay_limit=30;
for(let i=0;i<wd_amt.length;i++){
   if(type=="upi"){ 
    if(wd_amt[i]<=upi_limit) {
        if(wd_amt[i]<=balance ){
        rem_balance -=wd_amt[i];
            }
        else {rem_balance=-1;
            break;
             }
    }
    else{
        rem_balance=-2;
        break;
    }
}
    else if(type=="atm"){ 
        if(wd_amt[i]<=atm_limit) {
            if(wd_amt[i]<=balance ){
            rem_balance -=wd_amt[i];
                }
            else {rem_balance=-1;
                break;
                 }
        }
        else{
            rem_balance=-2;
            break;
        }
    }
    else if(type=="tap_to_pay"){ 
        if(wd_amt[i]<=tap_to_pay_limit) {
            if(wd_amt[i]<=balance ){
            rem_balance -=wd_amt[i];
                }
            else {rem_balance=-1;
                break;
                 }
                }
                else{
                    rem_balance=-2;
                    break;
                }
            }
    else {
        rem_balance=-2;
        break;
    }
    
    }
    return rem_balance;
}


let bal=70;
let amt = [30,2,3,4];
let type="upi";
res=Withdrawl(bal,amt,type);
if(res==-1){
    console.log("Withdrawl Amt. Exceeded than balance");
}
else if(res==-2){
    console.log("Withdrawl Amt. Exceeded than type limit");
}
else if(res==-3){
    console.log("Invalid Type");
}
else 
console.log(res);
