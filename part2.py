"""
                Student Name  -  Sandeepa Perera
                Student ID    -  2017184
                Date          -  July 2021
"""

#Software Development - Course Work part 11


def credits():
    #using while loop for make a loop
    while True:
        
        
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
                        if (credit_total>=120): # check total

                            if (credit==120 and defer==0 and fail==0):
                                print("Progress")

                                                                        #progress and module trailer
                            elif (credit==100 and (defer +fail)==20):
                                 print("Progress (module trailer)")

                                                                         #Do not Progress-module retriever
                            elif ((credit + defer )<=120 and fail<=60):
                                print("Do not Progress-module retriever")
                                
                            elif ((credit + defer )<=40 and (80<=fail<=120)): #Exclude
                                print("Exclude")


                        else:
                            print("Total incorrect") # if total check wrong print statement
                        
                    else:
                        print ("Out of range")
                else:
                   print ("Out of range")     
            else:
                print ("Out of range")

               
                    
        except:
            print("Integer required")
            continue       # after the comments loop will continueing
             
            
credits()
