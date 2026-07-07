
# employee management  system : 

"""
1. add employee
2. delete employee
3. update employee
4. display employee
"""
d1={}
def add_employee():
    id =int(input("enter id : "))
    name =input("enter name : ")
    salary =int(input("enter salary : "))
    age =int(input("enter age : "))
    d1[id] =[name,salary,age]
    
def update_employee():
    id =int(input("enter id : "))
    if  id in d1 :
        update_name =input("enter new name : ")
        update_salary =int(input("enter new salary : "))
        d1[id]=[update_name,update_salary,d1[id][2]]
    else :
        print("id not found")

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
    
def main():
    while True:
        print("1. add employee")
        print("2. delete employee")
        print("3. update employee")
        print("4. display employee")
        print("5. exit")
        choice =int(input("enter choice : "))
        match choice :
            case 1 :
                add_employee()
            case 2 :
                delete_employee()
            case 3 :
                update_employee()
            case 4 :
                display_employee()
            case 5 :
                break
main()
    
      
# bank  app  () : 