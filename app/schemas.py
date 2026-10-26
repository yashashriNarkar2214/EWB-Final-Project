from pydantic import BaseModel, EmailStr
from typing import Optional

class StudentCreate(BaseModel):
    student_name: str
    dob: str
    email: EmailStr
    phone: Optional[str] = None
    course: Optional[str] = None
    address: Optional[str] = None
    enrollment_date: Optional[str] = None

class StudentUpdate(BaseModel):
    student_name: Optional[str] = None
    dob: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    course: Optional[str] = None
    address: Optional[str] = None
    enrollment_date: Optional[str] = None

class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True