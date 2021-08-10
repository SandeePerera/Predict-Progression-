"""
                Student Name  -  Sandeepa Perera
                Student ID    -  2017184
                Date          -  July 2021
"""

#Software Development - Course Work part 111

count1=0
count2=0
count3=0
count4=0
total=0
cont=0
defer=0
credit=0
fail=0

def credits():
    global credit
    global defer
    global fail
    global credit_total

    try:
        #get credits at pass
        credit=int(input("Please enter your credit at pass : ")) 
        if (credit==0 or credit==20 or credit==40 or credit==60 or credit==80 or credit==100 or credit==120):

            #get credits at defer
            defer=int(input("Please enter your credit at defer : ")) 
            if (defer==0 or defer==20 or defer==40 or defer==60 or defer==80 or defer==100 or defer==120):

                #get credits at fail
                fail=int(input("Please enter your credit at fail : "))  
                credit_total=(credit+defer+fail)
                if (fail==0 or fail==20 or fail==40 or fail==60 or fail==80 or fail==100 or fail==120):

                    if (credit_total>120):      # cheack total
                        print("Incorrect Total")
                       
                else:
                    print ("Out of Range")
                       
            else:
                print("Out of Range")
                b
        else:
            print("Out of Range")
            
    except:
        print("Integer required")
        
    
credits()

credit_total=(credit+defer+fail)

while True:
                    
    if (credit==0 or credit==20 or credit==40 or credit==60 or credit==80 or credit==100 or credit==120):
        if (defer==0 or defer==20 or defer==40 or defer==60 or defer==80 or defer==100 or defer==120):
            if (fail==0 or fail==20 or fail==40 or fail==60 or fail==80 or fail==100 or fail==120):
                if (credit_total<=120):
                    
                    if (credit==120 and defer==0 and fail==0):
                        print("Progress")
                        count1+=1
                        
                                    
                                                                            #progress and module trailer
                    elif (credit==100 and (defer +fail)==20):
                        print("Progress (module trailer)")
                        count2+=1
                      
                                                                             #Do not Progress-module retriever
                    elif ((credit + defer )<=120 and fail<=60):
                        print("Do not Progress-module retriever")
                        count3+=1
                        
                                    
                    elif ((credit + defer )<=40 and (80<=fail<=120)): #Exclude
                        print("Exclude")
                        count4+=1
               
                
                        

                    cont=input('''Would you like to enter another set of data?/nEnter 'y' for yes or 'q' to quit and view results: ''')

                    if cont=="y":
                        credits()
                    else:
                        print("Progress",count1,":","*"*count1)
                        print("Progress",count2,":","*"*count2)
                        print("Progress",count3,":","*"*count3)
                        print("Progress",count4,":","*"*count4)
        

                        total=(count1+count2+count3+count4)
                        print("")

                        print(total," outcomes in total")
               
                        break
                                    

                            
                    
