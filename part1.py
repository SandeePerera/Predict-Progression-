"""
                Student Name  -  Sandeepa Perera
                Student ID    -  2017184
                Date          -  July 2021
"""

#Software Development - Course Work part 1


credit=int(input("Please enter your credit at pass : ")) #Get credits at pass
defer=int(input("Please enter your credit at defer : ")) #Get credits at defer
fail=int(input("Please enter your credit at fail : "))  #Get credits at fail

                                            #progress
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

                            #Invalid Inputs
else:
    print ("Invalid Inputs")
    
                

        
                
                    
            

        
       
                    
    
