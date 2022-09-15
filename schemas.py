from pydantic import BaseModel

class Employee(BaseModel):
    emp_name:str
    dept:str
