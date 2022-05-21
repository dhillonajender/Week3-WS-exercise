class Student:
    global student_detail
    student_detail = []
    
    def __init__(self,student_id,student_name,student_grades=[]):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__student_grades = student_grades
    
    def set_student_id(self,student_id):
        self.__student_id = student_id
    def get_student_id(self):
        return self.__student_id
    
    def set_student_name(self,student_name):
        self.__student_name = student_name
    def get_student_name(self):
        return self.__student_name
    
    def set_student_grades(self,student_grades):
        self.__student_grades = student_grades
    def get_student_grades(self):
        return self.__student_grades

def add_student(student): #student object
    for i in range(len(student.get_student_grades())):
        if(0.0<=student.get_student_grades()[i]<=100.0 and (len(str(student.get_student_id()))== 7) ):
            if(len(student.get_student_grades()) == i+1): #travesing thru the list and when its finishes add that details
                student_detail.append(student)
                print("Student added successfully")
                break
        else:
            print("Invalid grades or Invalid number")
            break
     
def update_student(student):#student object
    count=0
    for i in range(len(student_detail)): #checking it with the id
        if(student.get_student_id() == student_detail[i].get_student_id()):
            student_detail[i].set_student_id(student.get_student_id())
            student_detail[i].set_student_name(student.get_student_name())
            student_detail[i].set_student_grades(student.get_student_grades())
            count+=1
    if(count==0):
        print("No student record exists to update")
    else:
        print("Student details updated successfully")
 
def delete_student(ip):#student_id or student_name
    count=0
    for i in range(len(student_detail)): #checking it with the id or name
        if((ip == student_detail[i].get_student_id()) or (ip == student_detail[i].get_student_name())):
            student_detail.pop(i)
            count+=1
    if(count==0):
        print("No student record exists to delete")
    else:
        print("Student details deleted successfully")

def search_student(ip):#student_id or student_name
    count=0
    for i in range(len(student_detail)): #checking it with the id or name
        if((ip == student_detail[i].get_student_id()) or (ip == student_detail[i].get_student_name())):
            print("Student ID: "+ str(student_detail[i].get_student_id()))
            print("Student NMAE: "+student_detail[i].get_student_name())
            print("Student Grades: "+ str(student_detail[i].get_student_grades()))
            count+=1
    if(count==0):
        print("No student record exists to search")
           
        
s1 = Student(3004325,"Ajender Singh",[67,82,90,99])
s2= Student(3002345,"Aksahy Agarwal",[67,81,99,95])
s3= Student(3002145,"Aks Agarwal",[67,51,88,95])
action = "add"

if(action =="add"):
    add_student(s1)
elif(action =="delete"):
    delete_student(s2.get_student_name())#student_id or student_name
elif(action =="search"):
    search_student(s3.get_student_id())#student_id or student_name
elif(action =="update"):
    update_student(s3)
else:
    print("Invalid option")
    



