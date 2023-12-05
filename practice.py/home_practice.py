
contacts={}
def contact_add(name,phone,email):
    contacts[name]={"phone": phone,"email":email} 
    print (f"{name}added successfullly")
    

def dispaly_contact(name):
        if name in contacts:
            contact_info=contacts[name]
            print(f"{name } alerady in the dictionary")
            print(f"Phone number is {contact_info['phone']}")
            print(f"Email is {contact_info['email']}")
        else:
                print (f"{name} not in list")
contact_add('Alice','6514001211','alice29@gmail.com')
contact_add('Robert','6127071406','robert99@yahoo.com')    
             
dispaly_contact("Alice")

      

      


