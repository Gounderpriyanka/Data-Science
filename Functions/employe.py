"""
bank app  : 

1. create  account :
    create  a  user name  : dishant 
    create  a  password  : dish@1211D    ===> 1 uppercase , 1 lowercase , 1 digit , 1 special character

2. login : 
        enter user name  : dishant 
        enter password  : dish@1211D
            ====> print  login success   ====> ac 25000 
            
1. deposit  
2. withdraw   : min balace 10000 maintain 
3. check balance 
4. exit 
"""

emp_account = []
user = ""

def create_password(password):
    
    if len(password)>=8 :
        lower =False
        upper =False
        digit =False
        special =False
        
        special_char =["@","#","$","%","^","&","*"]
        
        for  i in password :
            if  i.isupper() :
                upper =True
            elif  i.islower() :
                lower =True
            elif  i.isdigit() :
                digit =True
            elif  i in special_char :
                special =True
        
        if  upper and lower and digit and special :
            return True
        else :
            return False
    else :
        return False

def create_account():
    global user
    
    print("----------create account ----------")
    
    username =input("enter username : ")
    password =input("enter password : ")
    
    if  create_password(password) :
        emp_account.append( {
            "username" : username,
            "password" : password,
            "balance" : 25000
        })

        print("account created successfully")
    else :
        print("password is not valid")
        
def login():
    global user
    
    username =input("enter username : ")
    password =input("enter password : ")
    
    for account in emp_account :
        if account["username"] == username:
            if account["password"] == password:
                user = username
                print("Login Success") 
        else: 
            print("password is not valid")
    else :
        print("username is not valid") 


        
def add_employee():
    id =int(input("enter id : "))
    name =input("enter name : ")
    salary =int(input("enter salary : "))
    age =int(input("enter age : "))
    emp_account.append( { "id":id,
                        "name":name,
                        "salary":salary,
                        "Age":age})
    
c

def delete_employee():
    id =int(input("enter id : "))
    if  id in d1 :
        del d1[id]
    else :
        print("id not found")
        
def display_employee():
    # logic
    id =int(input("enter id : "))
    if  id in d1 :
        print(d1[id])
    else :
        print("id not found")
    
# def main():
#     while True:
#         print("1. add employee")
#         print("2. delete employee")
#         print("3. update employee")
#         print("4. display employee")
#         print("5. exit")
#         choice =int(input("enter choice : "))
#         match choice :
#             case 1 :
#                 add_employee()
#             case 2 :
#                 delete_employee()
#             case 3 :
#                 update_employee()
#             case 4 :
#                 display_employee()
#             case 5 :
#                 break
# main()
    
      
# bank  app  () : 

add_employee()
add_employee()
add_employee()
print(emp_account)