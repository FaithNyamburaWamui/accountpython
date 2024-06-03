class Student:
    school="AkiraChix"

    def __init__(self, first_name, last_name, age, country, code):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country  = country
        self.code=code
        
    def greet_student(self):
        greetings=f"Hello {self.first_name}, welcome to {self.school}. Your code is {self.code} "

        return greetings

    def year_of_birth(self):
        return f"Hello {self.first_name} you are born in {2024-self.age}"
    
    def full_name(self):
        return f"Hello my name is {self.first_name} {self.last_name}"
    
    def initials(self):
        return f"My initials are {self.first_name[0]} {self.last_name[0]}"
    
    def check_minor(self):
         if self.age<=18:
             print("You are a minor")
         else:
             print("You are not a minor")

        
    def enroll_student(self):
        if self.age<=5:
            print("You are in the classes between 1-5")
        elif self.age<=12:
            print("You are in classes between 6-8")
        else:
            print("You are in classes between 41-44")

    def students(self, course, enrollment_date):
        print(f"You {self.first_name} {self.last_name} have enrolled in {course} on {enrollment_date}")








    
