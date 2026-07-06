class student:
    print("Welcome to Student Management System")

    def newdata(self):
        while True:
            self.name = input("Enter Student Name: ")
            if self.name.replace(" ","").isalpha():
                break
            else:
                print("Name should be in Letters\n")
        while True:
            self.fatname = input("Enter Father's Name: ")
            if self.fatname.replace(" ","").isalpha():
                break
            else:
                print("Father's Name should be in Letters\n")
        while True:
            self.motname = input("Enter Mother's Name: ")
            if self.motname.replace(" ","").isalpha():
                break
            else:
                print("Mother's Name should be in Letters\n")

        while True:
            try:
                self.age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Age should be a number. Please enter again.\n")

        with open("C:/Users/Lenovo/OneDrive/Desktop/NCC & TSC Material/student.txt", "a") as f:
            f.write(f"Name: {self.name} | Father Name: {self.fatname} | Mother Name: {self.motname} | Age: {self.age}\n")
        print("New Data Successfully Entered!!!")

            
    def update(self):
        with open("C:/Users/Lenovo/OneDrive/Desktop/NCC & TSC Material/student.txt", "r") as b:
            a = b.readlines() 
            print("Existing Records...")
            for j, i in enumerate(a, start=1):
                print(j," | ", i)

            while True:
                    try:
                        self.select = int(input("Enter the Serial Number of Student: "))
                        if self.select > len(a):
                            print("Serial Number Exceeds")
                        else:
                            break
                    except ValueError:
                        print("Serial Number should be an integer.")
                   
            while True:
                self.name = input("Enter Student Name: ")
                if self.name.replace(" ","").isalpha():
                    break
                else:
                    print("Name should be in Letters\n")
            while True:
                self.fatname = input("Enter Father's Name: ")
                if self.fatname.replace(" ","").isalpha():
                    break
                else:
                    print("Father's Name should be in Letters\n")
            while True:
                self.motname = input("Enter Mother's's Name: ")
                if self.motname.replace(" ","").isalpha():
                    break
                else:
                    print("Mother's Name should be in Letters\n") 
            
            while True:
                try:
                    self.age=int(input("Enter Student Age:"))
                    break

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
            for j, i in enumerate(line, start=1):
                print(j," | ", i)

            while True:
                try:
                    self.select1=int(input("Enter the Serial Number of Student:"))
                    break
                except ValueError:
                    print("Serial Number should be Number")

            while True:
                try:
                    line[self.select1-1] =""
                    break
                except IndexError:
                    print("No Data is in File")
                

            with open("C:/Users/Lenovo/OneDrive/Desktop/NCC & TSC Material/student.txt", "w") as g:
                g.writelines(line)
            print("Record Deleted Successfully !!!")
            
    def Total(self):
        with open("C:/Users/Lenovo/OneDrive/Desktop/NCC & TSC Material/student.txt","r") as d:
            print(f"Total Number of Record : {len(d.readlines())}")

p1=student()
def class_control():        
        while True:
            pw=input("Enter the Password:")
            if pw=="python":
                print("Correct Password\n")
                break
            else:
                print("Incorrect Password\n")
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
                    print("""THANK YOU !!!\n
                    "Your Data is Saved in student.txt file""" )
                    break 
            except ValueError:
                print("Choice Should be from 1,2,3,4 and Integer Value")

class_control()
