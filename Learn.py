#  Online Learning Platform
# Problem Statement: Build a class hierarchy for an online learning platform. The base class User includes name and email. 
# The subclass Instructor adds subject expertise and a method to upload content. 
# A third class CourseCreator (inherits from Instructor) allows creation of complete courses with modules. 
# Override the display_info() method at each level to reflect role-specific details.
class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    
    def display_info(self):
        print(f"User:\n Name: {self.name} , email: {self.email}")


class Instructor(User):
    def __init__(self, name, email,subject_expertise):
        super().__init__(name, email)
        self.subject_expertise=subject_expertise
            
    def display_info(self):
         print(f"Instructor:\n Name: {self.name} , email: {self.email} , subject expertice: {self.subject_expertise}")
        
    def upload_content(self,course_name,course_content):
        print(f"course contern {course_content} added to {course_name}")
        
class CouraeCreator(Instructor):

    def __init__(self, name, email, subject_expertise):
        super().__init__(name, email, subject_expertise)
        self.course_created=0

    def create_course(self,course_name,no_of_moudles):
        list_of_modules=[]
        for i in range(1,no_of_moudles+1):
            module=input(f"enter moduel {i}:")
            list_of_modules.append(module)
        self.course_created+=1
        return {course_name:list_of_modules}
    
    def display_info(self):
        print(f"Course creator:\n Name: {self.name} , email: {self.email} , subject expertice: {self.subject_expertise} , courses created :{self.course_created}")


u=User('vishnu','v@gmail.com')
u.display_info()

instructor1=Instructor('vinay',"v1@gmmail.com","cse")
instructor1.display_info


course_creator1=CouraeCreator('rishi','ri@gmail.com','physics')
course_creator1.display_info()
course_creator1.create_course('light',2)
course_creator1.display_info()