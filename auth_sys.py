def password(username,lp1,lp2,lp3):
    pswrd=input("Enter the password: ")
    if(len(pswrd)>=10 and pswrd!=lp1 and pswrd!=lp2 and pswrd!=lp3):
        up_ct=0    #upper count
        lo_ct=0    #lower count
        no_ct=0    #number count
        sp_ct=0    #special character count
        uniq_ct=0 #upper count
        for i in range(len(pswrd)):
            if(pswrd[i]>="A" and pswrd[i]<="Z"):  #to count the upper characters
                up_ct+=1  
            elif(pswrd[i]>="a" and pswrd[i]<="z"): #to count the lower characters
                lo_ct+=1
            elif(pswrd[i]>="0" and pswrd[i]<="9"): #to count the numbers(digits)
                no_ct+=1
            # elif(pswrd[i] >= "33" and pswrd[i] <= "47" and pswrd[i] >= "58" and pswrd[i] <= "64" and pswrd[i] >= "91" and pswrd[i] <= "96" and pswrd[i] >= "123" and pswrd[i] <= "126"):
            elif pswrd[i] in "#$%&'()*+,-./:;<=>?@[\]^_`{|}~": #to count the special characters
              sp_ct+=1
            if( (i+4)<len(pswrd) and pswrd[i]==pswrd[i+1] and pswrd[i]==pswrd[i+2] and pswrd[i]==pswrd[i+3] and pswrd[i]==pswrd[i+4] ):
                uniq_ct+=1 
                #So that no character should repeat more than three times in a row
            if username and pswrd[i:i+3] in username:
                print("Invalid Password!,try again")
                password(username,lp1,lp2,lp3)   
                     # "Password should not contain any sequence of three or more consecutive characters from the username."
        if(up_ct>=2 and lo_ct>=2 and no_ct>=2 and sp_ct>=2 and uniq_ct==0):
            print("password accepted") #show message of password acceptance whenever the password meet all criteria
        else:
            print("Invalid Password!,try again") #show message of password rejection
            password(username,lp1,lp2,lp3)       #giving another try to user
    else:
        print("Invalid Password!,try again")  #show message of password rejection
        password(username,lp1,lp2,lp3)        #giving another try to user
username=input("Enter the username:")       #taking input of username from the user
lp1=input("Enter the last password 1: ")    #taking input of last 3 passwords from the user
lp2=input("Enter the last password 2: ")
lp3=input("Enter the last password 3: ")
password(username,lp1,lp2,lp3)