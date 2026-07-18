account = []
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
        account[username] = {
            
            "password" : password,
            
        }

        print("account created successfully")
    else :
        print("password is not valid")
        
def login():
    global user
    
    username =input("enter username : ")
    password =input("enter password : ")
    
    if username in account :
        if account[username]["password"] == password:
            user = username
            print("Login Success") 
        else: 
            print("password is not valid")
    else :
        print("username is not valid") 