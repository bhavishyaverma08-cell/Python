def password(n):
    if n=="Python":
        print("Correct Password")
        class student:
            print("Welcome to Student Management System")

            def newdata(self):
                try:
                    self.name=input("Enter Student Name:")
                    self.fatname=input("Enter Father's Name:")
                    self.motname=input("Enter Mother's Name:")   
                except ValueError:
                    print("Name should be letters not numbers")
                try:
                    self.age=int(input("Enter Student Age:"))
                except ValueError :
                    print("Age should be number")
                with open("C:/Users/Lenovo/OneDrive/Desktop/NCC & TSC Material/student.txt","a") as f:
                    f.write(f"Name: {self.name} | Father Name: {self.fatname} | Mother Name: {self.motname} | Age: {self.age}\n")
                print("New Data Successfully Enter !!!")

            
            def update(self):
                with open("C:/Users/Lenovo/OneDrive/Desktop/NCC & TSC Material/student.txt", "r") as b:
                    a = b.readlines() 
                    print("Existing Records...")
                    for i in a:
                        print(i)
                    
                    try:
                        self.select=int(input("Enter the Serial Number of Student:"))
                        if self.select > len(a):
                            print("Serial Number Exceeds")
                            return                        
                    except ValueError:
                        print("Serial Number should be Integer")
                    
                    try:
                        self.name=input("Enter Student Name:")
                        self.fatname=input("Enter Father's Name:")
                        self.motname=input("Enter Mother's Name:")   
                    except ValueError:
                        print("Name should be letters not numbers")
                    try:
                        self.age=int(input("Enter Student Age:"))
                    except ValueError :
                        print("Age should be number")

                    try:
                        a[self.select-1] = (
                        f"Name: {self.name} | "
                        f"Father Name: {self.fatname} | "
                         f"Mother Name: {self.motname} | "
                        f"Age: {self.age}\n"
                        )
                    except IndexError:
                        print("No Data is in File")
                        return

                with open("C:/Users/Lenovo/OneDrive/Desktop/NCC & TSC Material/student.txt", "w") as h:
                    h.writelines(a)

                print("Successfully Updated!!!")

            
            def delete(self):
                with open("C:/Users/Lenovo/OneDrive/Desktop/NCC & TSC Material/student.txt","r") as c:
                    line=c.readlines()
                    for i in line:
                        print(line)
                    try:
                        self.select1=int(input("Enter the Serial Number of Student:"))
                    except ValueError:
                        print("Serial Number should be Number")
                    
                    try:
                        line[self.select1-1] =""
                    except IndexError:
                        print("No Data is in File")
                        return

                with open("C:/Users/Lenovo/OneDrive/Desktop/NCC & TSC Material/student.txt", "w") as g:
                    g.writelines(line)
                print("Record Deleted Successfully !!!")
            
            def Total(self):
                with open("C:/Users/Lenovo/OneDrive/Desktop/NCC & TSC Material/student.txt","r") as d:
                    print(f"Total Number of Record : {len(d.readlines())}")

        p1=student()
        
        while True:
            print("1-Insert New Data | 2-Update Record | 3-Delete the Record | 4-Find Total Record | 5-Exit")
            try:
                choice=int(input("Enter The Choice:"))
                if choice==1:
                    p1.newdata()
                elif choice==2:
                    p1.update()
                elif choice==3:
                    p1.delete()
                elif choice==4:
                    p1.Total()
                elif choice==5:
                    print("THANK YOU !!!")
                    break 
                
            except ValueError:
                print("Choice Should be from 1,2,3,4 and Integer Value")
            
    else:
        print("Incorrect Password")
password(input("Enter the Password:"))
