def password(username,lp1,lp2,lp3):
    pswrd=input("Enter the password: ")
    if(len(pswrd)>=10):
        if(pswrd!=lp1):
            if(pswrd!=lp2):
              if(pswrd!=lp3):
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
                    elif(pswrd[i] in "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"): #to count the special characters
                      sp_ct+=1
                    if( (i+4)<len(pswrd) and pswrd[i]==pswrd[i+1] and pswrd[i]==pswrd[i+2] and pswrd[i]==pswrd[i+3] and pswrd[i]==pswrd[i+4] ):
                        uniq_ct+=1   #So that no character should repeat more than three times in a row     

              else: 
                  print("password should not be equals to previous password 3")           #showing error message
                  password(username,lp1,lp2,lp3)                                          #giving user another try
            else:
                 print("password should not be equals to previous password 2")  
                 password(username,lp1,lp2,lp3)             
        else:
            print("password should not be equals to previous password 1")   
            password(username,lp1,lp2,lp3)        
    else:
        print("Password length should be atleast 10") 
        password(username,lp1,lp2,lp3)    
        
    if(up_ct>=2):
           if(lo_ct>=2):
                if(no_ct>=2):
                    if(sp_ct>=2):
                        if(uniq_ct==0):
                            if pswrd[i:i+3] in username:
                                 print("password accepted")
                            else:
                                 print("The password should not contain any sequence of three or more consecutive characters from the username") 
                                 password(username,lp1,lp2,lp3) 
                        else:
                          print("no character should repeat more than three times in a row") #show message of password rejection
                          password(username,lp1,lp2,lp3)       #giving another try to user
                    else: 
                        print("Password must contain atleast 2 special characters.")
                        password(username,lp1,lp2,lp3)       #giving another try to user
                else: 
                    print("Password must contain atleast 2 numbers(digits).")   
                    password(username,lp1,lp2,lp3)       #giving another try to user     
           else:
                print("Password must contain atleast 2 lower characters.") 
                password(username,lp1,lp2,lp3)       #giving another try to user          
    else:
            print("Password must contain atleast 2 upper characters.")  
            password(username,lp1,lp2,lp3)       #giving another try to user 
username=input("Enter the username:")       #taking input of username from the user
lp1=input("Enter the last password 1: ")    #taking input of last 3 passwords from the user
lp2=input("Enter the last password 2: ")
lp3=input("Enter the last password 3: ")
password(username,lp1,lp2,lp3)