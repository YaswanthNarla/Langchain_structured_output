from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):

    name: str = 'nitish' #Here name and age are default values.
    age: Optional[int] = None #set Optional Value like this
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


new_student = {'age':32, 'email':'abc@gmail.com'} # dict with optional value

student = Student(**new_student) #Object creation with optional value 

student_dict = dict(student)

print(student_dict['age'])  

student_json = student.model_dump_json()