from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from langchain_ollama import ChatOllama
from app.database import get_db
from app.models import Student

router = APIRouter(prefix="/students", tags=["AI Extension"])

# Initialize local Ollama model (Make sure 'ollama serve' and 'ollama pull llama3.2' are run)
llm = ChatOllama(model="llama3.2")

SYSTEM_PROMPT = """
You are a helpful assistant for a student management database system. 
Use the provided student database records to answer the user's question accurately, professionally, and concisely.
"""

@router.post("/query-ai")
def query_local_ai(user_question: str, db: Session = Depends(get_db)):
    students = db.query(Student).all()
    db_records = "\n".join([
        f"ID: {s.id}, Name: {s.student_name}, DOB: {s.dob}, Email: {s.email}, Course: {s.course}, Enrolled: {s.enrollment_date}"
        for s in students
    ])
    
    prompt = f"{SYSTEM_PROMPT}\n\nDatabase Records:\n{db_records}\n\nUser Question: {user_question}"
    response = llm.invoke(prompt)
    
    return {
        "status": "success",
        "question": user_question,
        "response": response.content
    }