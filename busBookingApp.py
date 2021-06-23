from busbook import*
import random

def getRouteId():
    print()
    print()
    print()
    myCursor.execute("select * from route")
    allRoutes=myCursor.fetchall()
    #print(allRoutes)
    print("""
                All Routes
            =====================""")

    j=1
    for i in allRoutes:
        print(j,i[1])
        j+=1

    selectRoute=int(input("Select Route By Serial No. :-"))
    routeId=allRoutes[selectRoute-1][0]
    print(routeId)
    return routeId

    
    
def getUserId():
    print()
    print()
    print()
    print("""
                For Varification Purpose..!""")
    passwd=input("Enter your Password again:")
    myCursor.execute("select * from u_profile where password='{}' ".format(passwd))
    User=myCursor.fetchone()
    print("Welcome {}".format(User[1].upper()))
    print("Your Id :",User[0])
    return User[0]

    

    

def selectRoute():
    print()
    print()
    print()
    myCursor.execute("select * from route")
    allRoute=myCursor.fetchall()

    y=1
    for i in allRoute:
        print(y,i[1])
        y+=1

    From=int(input(" Select Route By No. (FROM) :"))
    To=int(input("Select Route By No. (TO) :"))

    
    if To==1:
        myCursor.execute("select b_name from bus where route_id='1'")
        uId=myCursor.fetchall()
        #print(uId)
        print("""
                            Available Busses for your Route
                     ======================================""")
        
        print()

        j=1
        for i in uId:
            print(j,i[0])
            j+=1
        inp=int(input("Select Bus :"))
        if inp==1:
            selectedBus=uId[0]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==2:
            selectedBus=uId[1]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==3:
            selectedBus=uId[2]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        else:
            print("Invalid Input")
    
            

    elif To==2:
        myCursor.execute("select b_name from bus where route_id='6'")
        uId=myCursor.fetchall()
        #print(uId)
        print("""
                            Available Busses for your Route
                     ======================================""")
        print()

        j=1
        for i in uId:
            print(j,i[0])
            j+=1
        inp=int(input("Select Bus :"))
        if inp==1:
            selectedBus=uId[0]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==2:
            selectedBus=uId[1]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==3:
            selectedBus=uId[2]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        else:
            print("Invalid Input")
            

    elif To==3:
        myCursor.execute("select b_name from bus where route_id='5'")
        uId=myCursor.fetchall()
        #print(uId)
        print("""
                            Available Busses for your Route
                     ======================================""")
        print()

        j=1
        for i in uId:
            print(j,i[0])
            j+=1
        inp=int(input("Select Bus :"))
        if inp==1:
            selectedBus=uId[0]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==2:
            selectedBus=uId[1]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==3:
            selectedBus=uId[2]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        else:
            print("Invalid Input")
            

    elif To==4:
        myCursor.execute("select b_name from bus where route_id='7'")
        uId=myCursor.fetchall()
        #print(uId)
        print("""
                            Available Busses for your Route
                     ======================================""")
        print()

        j=1
        for i in uId:
            print(j,i[0])
            j+=1
        inp=int(input("Select Bus :"))
        if inp==1:
            selectedBus=uId[0]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==2:
            selectedBus=uId[1]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==3:
            selectedBus=uId[2]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        else:
            print("Invalid Input")
            

    elif To==5:
        myCursor.execute("select b_name from bus where route_id='3'")
        uId=myCursor.fetchall()
        #print(uId)
        print("""
                            Available Busses for your Route
                     ======================================""")
        print()

        j=1
        for i in uId:
            print(j,i[0])
            j+=1
            
        inp=int(input("Select Bus :"))
        if inp==1:
            selectedBus=uId[0]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==2:
            selectedBus=uId[1]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        else:
            print("Invalid Input")
            
    elif To==6:
        myCursor.execute("select b_name from bus where route_id='4'")
        uId=myCursor.fetchall()
        #print(uId)
        
        print("""
                            Available Busses for your Route
                     ======================================""")
        

        j=1
        for i in uId:
            print(j,i[0])
            j+=1
            
        inp=int(input("Select Bus :"))
        if inp==1:
            selectedBus=uId[0]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==2:
            selectedBus=uId[1]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==3:
            selectedBus=uId[2]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        else:
            print("Invalid Input")

    elif To==7:
        myCursor.execute("select b_name from bus where route_id='2'")
        uId=myCursor.fetchall()
        #print(uId)
        
        print("""
                            Available Busses for your Route
                     ======================================""")
        

        j=1
        for i in uId:
            print(j,i[0])
            j+=1
            
        inp=int(input("Select Bus :"))
        if inp==1:
            selectedBus=uId[0]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==2:
            selectedBus=uId[1]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        elif inp==3:
            selectedBus=uId[2]
            print("You Selected",selectedBus[0])
            return selectedBus[0]
        else:
            print("Invalid Input")
#=================================================================Existing User======================================================================            
def Existing_user():
    print()
    print()
    print()
    uname=input ("Enter User Name:-")
    pswd=input("Enter Password :-")

    myCursor.execute("select * from u_profile where u_name='{}' and password='{}' ".format(uname,pswd))
    userData=myCursor.fetchone()
    #print(userData)

    if userData:
        print("Welcome {}".format(userData[1].upper()))
        if userData[5]=="admin":
            Admin()
        elif userData[5]=="customer":
            Customers()
    else:
        print("Invalid Username Or Password..Try again")
   
#=================================================================New User===========================================================================    
def New_User():
    
   
    print("""
                            Create New Account
                     ======================================""")
    newName=input("Enter User Name :")
    passwd=input("Enter Password :")
    mobile=input("Enter Mobile No. :")
    age=int(input("Enter Your age :"))
    myCursor.execute("insert into u_profile(u_name,password,mobile,age,role) values('{}','{}','{}',{},'customer')".format(newName,passwd,mobile,age))
    myDB.commit()
    print("Account has been created sucessfully...")
    print("welcome")
    Customers()
        
#=============================================================ADMIN===================================================================================
def Admin():
    while True:
        print()
        print()
        print()

        print("1. Add Route :")
        print("2. Add Bus :")
        print("3. Logout :")
        ch=int(input("Enter Your Choice :"))

        if ch==1:
           rname=input("Enter Route Name :")
           myCursor.execute ("insert into route(r_name) values('{}')".format(rname))
           myDB.commit()
           myCursor.execute("select * from route")
           allrts=myCursor.fetchall()
           print("Rout has been added sucessfuly..")
           
           j=1
           for i in allrts:
               print(j,i[1])
               j+=1

        elif ch==2:
            routeId = getRouteId()
            
            myCursor.execute("select * from bus")
            allBuses=myCursor.fetchall()
            print()
            print("""
                            Available Buses
                     ======================================""")
            n=1
            for k in allBuses:
                print(n,k[1])
                n+=1
                
            bname=input("Enter Bus name :")
            myCursor.execute("insert into bus(b_name,route_id) values ('{}',{})".format(bname,routeId))
            myDB.commit()
            myCursor.execute("select * from bus")
            allbuses=myCursor.fetchall()
            #print("Bus Lists '{}'".format(allbuses))
            print("""
                             Bus List
                     ======================================""")

            j=1
            for i in allbuses:
                print(j,i[1])
                j+=1
            print("Bus has been added sucessfully...")
            
        elif ch==3:
            break
        else:
            print("Invalid selection")
#======================================================================================CUSTOMERS===========================================================
def Customers():
    while True:
        print()
        print()
        print()
        
        print("1. Booking Bus :")
        
        print("2. Check PNR Status :")

        print("3. Cancel Reserved Ticket :")
        
        print("4. Exit :")

        ch=int(input("Make Your Selection :-"))

        if ch==1:
            user_id=getUserId()

    
    #========================================Bus===========================
            bus_name=selectRoute()
            
            

    #========================================Date==========================

            date=input("Enter Date Of Journey (DD-MM-YYYY) :")

    #========================================No of Seats====================

            noOfSeats=int(input("Enter No of seats :"))
            

    #=====================================Amount============================
            amount=[460,600,976,432,597,349,665,700,810,623,481]
            value=random.choice(amount)
            print("Your Amount Is :-",value,"Rs")
            
    #=======================================================================      

            myCursor.execute("insert into pnr(user_id,bus_name,no_of_seats,journey_date,amount) values({},'{}',{},'{}',{})".format(user_id,bus_name,noOfSeats,date,value))
            myDB.commit()
            print("Your Ticket booked Sucessfully")

            
            
            
    #=========================================================================PNR STATUS ===============================================================
            
        
        elif ch==2:
            
                
            
            print("FOR VARIFICATION PORPUSE !")
            inp=int(input("Enter Your User Id :"))
            jdate=input("Enter Your Date of Journey :")
            
                    

                    
                    
            myCursor.execute("select * from pnr where user_id='{}'and journey_date='{}'".format(inp,jdate))
            PNR=myCursor.fetchall()

            try:
                inp==(PNR[0][1])
                    
                status=(" 1. Your Id :- {} \n 2. Bus Name :-{} \n 3. No. Of Seats :- {} \n 4. Date Of Journey:- {} \n 5. Total Amount :- {}".format(PNR[0][1],PNR[0][2],PNR[0][3],PNR[0][4],PNR[0][5]))
                print()
                print("Your PNR Status Is ....")
                print(status)
                print()
                print()
                #Customers()
            

            except: 
                print("Invalid user id..")
                #print("Enter again..")
                break

        elif ch==3:
            uId=int(input("Enter User Id :"))
            dNo=input("Enter Date Of journey :")

            myCursor.execute("delete from pnr where user_id='{}' and journey_date='{}'".format(uId,dNo))
            myDB.commit()

            print("Reserved Ticket Cancel Sucessfully..")
            

                
            

            

        else:
            
            break
        

    
#======================================================================================================================================================================================      
    
while True:
    print()
    print()
    print()

    print("1. Create New account ")
    print("2. Login")
    print("3. Exit")

        

    NewExe=input("Make your selection by No. :")
        
            
            
    if NewExe=="1":
        New_User()
    elif NewExe=="2":
        Existing_user()
    elif NewExe=="3":
        break
    else:
        print("Invalid selection Try again...")
        


    


    

